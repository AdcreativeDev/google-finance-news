import streamlit as st
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from PIL import Image



st.set_page_config(
    page_title="Finance Question",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


image = Image.open("google-stock.jpg")
st.image(image, caption='created by MJ')

st.title("❓:blue[Questions to answer before investing in a stock]")

system_openai_api_key = os.environ.get('OPENAI_API_KEY')
system_openai_api_key = st.text_input(":key: OpenAI Key :", value=system_openai_api_key)
os.environ["OPENAI_API_KEY"] = system_openai_api_key


system_serpapi_api_key = os.environ.get('SERPAPI_API_KEY')
system_serpapi_api_key ="2412a22f7b5670afb53a687e0432d84cad408de0ee6bfc11db9c76be08ffec71"
system_serpapi_api_key = st.text_input(":key: SERPAPI Key :", value=system_serpapi_api_key)
os.environ["SERPAPI_API_KEY"] = system_serpapi_api_key
st.write('you can get the API key from https://serpapi.com/')

with st.expander("sample"):
    image = Image.open("Finance-question.png")
    st.image(image, caption='Sample')


llm = OpenAI(temperature=0)

# tool to interact the world 
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# https://js.langchain.com/docs/modules/agents/agents/
# The agent you choose depends on the type of task you want to perform
# If you're using a text LLM, first try zero-shot-react-description
agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)


query1 = "list out the stock price of TSLA and performance comparsion over 3 years period"
query2 = "For stock code : AAPL  , Analysis this company. What are its EPS and P/E? Is the company profitable? What are its plans for the future? "
query3 = "Who are its competitors of OpenAI in 2022 and What are the similiar products from their competitors is offering ? "
query4 = "how many females have stayed more than 3 years? "
query5 = "how many females from city category A purchase product_Category_1 ?"
query6 = "What is the total number of Product Category_1 purchased by female from city category B whose age is 0-17 ?"

Qstr1 = "Stock cod TSLA background and price performance"
Qstr2 = "Analyze Stock Code : AAPL , Apple.com"
Qstr3 = "Who are its competitors of OpenAI? "
Qstr4 = "Leo DiCaprio's girlfriend?"
Qstr5 = "Purchase by gender, city and product"
Qstr6 = "Purchase by gender, city and age group"
Qstr7 = ""


finalQuery = "Select Query Type"
queryselection =st.radio ("**Step 1 : Select the  Question :** ",
                            (Qstr1, Qstr2, Qstr3))

# default choice
finalQuery = query1

if queryselection == Qstr1:
    finalQuery = query1

if queryselection == Qstr2:
    finalQuery = query2

if queryselection == Qstr3:
    finalQuery = query3

if queryselection == Qstr4:
    finalQuery = query4

if queryselection == Qstr5:
    finalQuery = query5
    

finalQuerySubmit = st.text_input('**Step 2 : You can amend it :** ', finalQuery)
st.write('Final Prompt Submit to Agnet : ')
st.warning(finalQuerySubmit)


if st.button("Submit",type='primary'):
    with st.spinner("Run Langchain chain ..."):
        st.write('✔️ load tools : serpapi , llm-math')
        st.write('✔️ Create LangChain agent')
        st.write('✔️ Agent execute the prompt')
        result=agent.run(finalQuerySubmit)
        st.write('✔️ Get Final Answer')
        st.subheader("Query Results:")
        st.success(result )



log = """
Prompt : list out the stock price of TSLA and performance comparsion over 3 years period
> Entering new  chain...
 I need to find the stock price of TSLA over the past 3 years
Action: Search
Action Input: "TSLA stock price 3 years"
Observation: Tesla, Inc. is an American multinational automotive and clean energy company headquartered in Austin, Texas. Tesla designs and manufactures electric vehicles, stationary battery energy storage devices from home to grid-scale, solar panels and solar roof tiles, and related products and services.
Thought: I need to find the stock price of TSLA over the past 3 years
Action: Search
Action Input: "TSLA stock price 3 years chart"
Observation: Tesla, Inc. is an American multinational automotive and clean energy company headquartered in Austin, Texas. Tesla designs and manufactures electric vehicles, stationary battery energy storage devices from home to grid-scale, solar panels and solar roof tiles, and related products and services.
Thought: I need to compare the stock performance of TSLA over the past 3 years
Action: Search
Action Input: "TSLA stock performance 3 years"
Observation: Tesla, Inc. is an American multinational automotive and clean energy company headquartered in Austin, Texas. Tesla designs and manufactures electric vehicles, stationary battery energy storage devices from home to grid-scale, solar panels and solar roof tiles, and related products and services.
Thought: I now know the final answer
Final Answer: Tesla, Inc. (TSLA) has seen a significant increase in stock price over the past 3 years, with a peak of $900 in January 2021.

> Finished chain.


Q: For stock code : AAPL  , Analysis this company. What are its EPS and P/E? Is the company profitable? What are its plans for the future? 
> Entering new  chain...
 I need to find out the financial information of the company
Action: Search
Action Input: "AAPL financial information"
Observation: Apple Inc. is an American multinational technology company headquartered in Cupertino, California. Apple is the world's largest technology company by revenue, with US$394.3 billion in 2022 revenue. As of March 2023, Apple is the world's biggest company by market capitalization.
Thought: I need to find out the EPS and P/E of the company
Action: Search
Action Input: "AAPL EPS and P/E"
Observation: As of today (2023-07-16), Apple's share price is $190.69. Apple's EPS without NRI for the trailing twelve months (TTM) ended in Mar. 2023 was $5.89. Therefore, Apple's PE Ratio without NRI for today is 32.38.
Thought: I need to find out if the company is profitable
Action: Search
Action Input: "AAPL profitability"
Observation: Apple net profit margin as of March 31, 2023 is 24.49%. Compare AAPL With Other Stocks ...
Thought: I need to find out the company's plans for the future
Action: Search
Action Input: "AAPL future plans"
Observation: The average price target for Apple is $189.17. This is based on 29 Wall Streets Analysts 12-month price targets, issued in the past 3 months. The highest analyst price target is $210.00 ,the lowest forecast is $149.00. The average price target represents 2.54% Increase from the current price of $184.48.
Thought: I now know the final answer
Final Answer: Apple's EPS and P/E are $5.89 and 32.38 respectively. The company is profitable with a net profit margin of 24.49%. The company's future plans include an average price target of $189.17, representing a 2.54% increase from the current price.

> Finished chain.




Q: Who are its competitors of OpenAI in 2022 and What are the similiar products from their competitors is offering ? 
> Entering new  chain...
 I need to research the competitors of OpenAI and their products
Action: Search
Action Input: "OpenAI competitors 2022"
Observation: OpenAI's top competitors include Inflection AI, Anthropic, and Stability AI. Inflection operates as an Artificial Intelligence(AI) studio which develops human-computer interaction. It enables users to speak to a computer program called Pi in a c…
Thought: I need to research the products of OpenAI's competitors
Action: Search
Action Input: "Inflection AI products"
Observation: We are an AI studio creating a personal AI for everyone. · Our first AI is called Pi, for personal intelligence, a supportive and empathetic conversational AI.
Thought: I now know the final answer
Final Answer: OpenAI's top competitors in 2022 are Inflection AI, Anthropic, and Stability AI. Inflection AI's products include Pi, a supportive and empathetic conversational AI.

> Finished chain.



"""


with st.expander("Log"):
    st.code(log)

