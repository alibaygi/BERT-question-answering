import streamlit as st
import requests
import json
#from annotated_text import annotated_text

st.set_page_config(
    page_title="Naturalangue",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown('<h1 style="text-align: center">SQuAD QA</h1>',
            unsafe_allow_html=True)

st.sidebar.header("Options")
top_k_reader = st.sidebar.slider("Max. number of answers",
                                 min_value=1, max_value=10, value=3, step=1)
top_k_retriever = st.sidebar.slider("Max. number of documents from retriever",
                                    min_value=1, max_value=10, value=3, step=1)


st.markdown('<h3>Question</h3>', unsafe_allow_html=True)
question = st.text_input(
    "Put your query", value="What is a Turing machine?")
button = st.button('Get Answer')
st.text("")
st.text("")

if button:
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
        'question': question, 'num_answers': top_k_reader, 'num_docs': top_k_retriever
    }
    response = requests.post('http://127.0.0.1:8080/query',
                             headers=headers,
                             data=json.dumps(data))
    ###
    result = json.loads(response.text)
    result_dict = result["answer"]["answers"]
    # st.write(result)
    st.subheader("Answers and Contexts")
    # for item in result["answer"]["answers"][item]
    for item in range(0, len(result_dict)):
        st.markdown(f"**Answer {item+1}**")
        # st.write(result_dict[item]["answer"])
        st.success(result_dict[item]["answer"])
        st.markdown(f"**Context {item+1}**")
        st.write(result_dict[item]["context"])


# before runing the following line main.py was executed. (uvicorn main:app  --port 8080)
# open a new terminal and cd UIApp
# streamlit run streamlit_qa.py (http://172.16.5.161:8501)
