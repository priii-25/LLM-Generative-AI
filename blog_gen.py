import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
import os
os.environ['OPENAI_API_KEY'] = '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'
# llm = OpenAI(temperature=0.9)
# title_chain = LLMChain(llm=llm, prompt = title_template, verbose = True, output_key='title')
title_template = PromptTemplate(
    input_variables = ['topic'], # web development using python
    template = 'Generate a SEO-friendly blog post title to on a technical blog on the topic - {topic}'
)
body_template = PromptTemplate(
    input_variables = ['title'],
    template = "Generate a 100 Words Short concise SEO worthy article on the given title - {title}"
)
llm = OpenAI(temperature=0.9) #LLaMa, Palm
title_chain = LLMChain(llm=llm, prompt=title_template, output_key="title")
body_chain = LLMChain(llm=llm, prompt=body_template, output_key="blog_init")
final_sequential_chain = SequentialChain(chains = [title_chain, body_chain], input_variables = ['topic'], output_variables = ['title','blog_init'], verbose=True)
st.title("Blog Generator")
prompt = st.text_input("Enter some keywords") # "Prompt goes here"
if prompt:
    with st.spinner("Generating"):
        response = final_sequential_chain({'topic': prompt})
        title = response.get('title')
        blog = response.get('blog_init')
        st.write(title)
        st.write(blog)
    
