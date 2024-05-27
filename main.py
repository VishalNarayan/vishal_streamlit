import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

with st.sidebar:
    st.write('hi')
    pass

# st.markdown(
#     """
# <style>
#     [data-testid="collapsedControl"] {
#         display: none
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )

st.write("This page is empty.")


