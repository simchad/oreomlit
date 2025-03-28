import streamlit as st


pg = st.navigation(
    {
    "Oreome": [
        st.Page("home.py", title="Home", icon="🔥"),
        st.Page("page_2.py", title="Second page", icon=":material/favorite:"),
        ],
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
        ],
    "Oreome Pipeline": [
        st.Page("OP_00_upload.py", title="Upload Data File"),
        st.Page("OP_01_corr.py", title="Correlation Analysis")
        ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
        ],
    }
)
pg.run()