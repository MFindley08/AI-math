import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="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")

st.set_page_config(page_title="Sum = Thin', Your Friendly Math Mentor")

openai_api_key = st.sidebar.text_input('OpenAI API Key', key="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", type='password')


prompt = """
Serve as a math and arithmetic reasoning guide, 
assisting students in resolving mathematical
inquiries. Students will present their questions, 
and your task is to methodically work through each 
problem, recording every logical step along the way. 
You may be prompted to reveal the solution or provide 
hints to guide students toward their own solution.

Here are some examples with answers and clues:

Question:  John has 5 apples, and Sarah gives him 3 more. 
How many apples does John have now?

Clues: To find the total number of apples John has now, add 
the apples he had initially (5) to the apples Sarah gave 
him (3).

Answer: John has 8 apples.

Question:  If the length of a rectangle is 8 cm and the width 
is 5 cm, what is its perimeter?
Clues: To find the perimeter of a rectangle, add the lengths 
of all four sides. For a rectangle, opposite sides are equal in length.
Answer: The perimeter of the rectangle is 26 cm.

Question: Solve for x: (1/2)x + 4 = 8.
Clues: To isolate x, first, subtract 4 from both sides of the equation. Then, multiply both sides by 2 (the reciprocal of 1/2).
Answer: x = 8.

Question: What is the next number in the sequence? 
Given Sequence: 2, 6, 18, 54, ...
Clues: Common Ratio: 3
Algorithm Application:
Input r = 3 and the last term, which is 54.
Calculate Next_term = 54 * 3 = 162.
Answer: The next term in the sequence is 162.

Question: {question}
"""


def generate_response(question):
    chat = ChatOpenAI(temperature=0.0, openai_api_key=openai_api_key)
    prompt_template = ChatPromptTemplate.from_template(template=prompt)
    messages = prompt_template.format_messages(
        question=question
    )
    response = chat(messages)
    return response.content

with st.form('myform'):
    question = st.text_input('Enter question:', '')
    clues = st.form_submit_button('Please give me clues')
    answer = st.form_submit_button('Please show me the answer')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if clues and openai_api_key.startswith('sk-'):
        st.info(generate_response(question).split("Clues")[1][2:])
    if answer and openai_api_key.startswith('sk-'):
        st.info(generate_response(question).split("Clues")[0])

