import streamlit as st
import pandas as pd

st.title('Process Capability Command Generator')

uploaded_file = st.file_uploader("Upload an Excel file", type=['xlsx', 'xls'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if 'Min' in df.columns and 'Max' in df.columns:
        commands = []
        for idx, row in df.iterrows():
            lspec = row['Min']
            uspec = row['Max']
            command = f"""Capa 'C{idx + 1}' 1;\nLspec {lspec};\nUspec {uspec};\nPooled;\nAMR;\nUnBiased;\nOBiased;\nToler 6;\nWithin;\nOverall;\nNoCI;\nPPM;\nCStat."""
            commands.append(command)

        command_output = "\n\n".join(commands)

        st.download_button(label="Download Commands", data=command_output, file_name="process_capability_commands.txt", mime="text/plain")

    else:
        st.error("Uploaded Excel file must contain 'Min' and 'Max' columns")
