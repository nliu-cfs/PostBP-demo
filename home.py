import streamlit as st
#layout setting
st.set_page_config(layout="wide")


# Customize the sidebar
markdown = """
Web App URL: <TBD>
GitHub Repository: <TBD>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/gusM05j.jpeg"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multipage app demonstrates various functions of the postDB library. 
    The postDB is an open-source project for postprocessing output of fire behavioural models
    """
)

st.header("Instructions")

markdown = """
1. 

"""

st.markdown(markdown)