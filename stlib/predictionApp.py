def run():
    import streamlit as st

    st.markdown("# Prediction App")
    st.sidebar.header("Prediction App")
    st.write(
    """This page is where we implement our prediction app"""
    )


# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()