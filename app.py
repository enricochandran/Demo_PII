import streamlit as st
import pandas as pd
from utils import mask_name, mask_email, mask_phone, mask_address, mask_purchase_id
import io

st.title("PII Masker")

uploaded_file = st.file_uploader("Unggah file CSV/XLS", type=["csv", "xls", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file, dtype=str)

    st.subheader("Preview Dataset")
    st.dataframe(df.head())

    if st.button("Masking PII"):
        df_masked = df.copy()

        columns_to_mask_and_suffix = {
            'Name': mask_name,
            'Email': mask_email,
            'Phone': mask_phone,
            'Address': mask_address
        }

        columns_to_mask_only = {
            'PurchaseID': mask_purchase_id
        }

        new_columns = []
        for col in df_masked.columns:
            if col in columns_to_mask_and_suffix:
                mask_function = columns_to_mask_and_suffix[col]
                df_masked[col] = df_masked[col].astype(str).apply(mask_function)
                new_columns.append(f"{col}_PII")
            # elif col in columns_to_mask_only:
            #     mask_function = columns_to_mask_only[col]
            #     df_masked[col] = df_masked[col].astype(str).apply(mask_function)
            #     new_columns.append(col)
            else:
                new_columns.append(col)

        df_masked.columns = new_columns

        st.subheader("Hasil Dataset Setelah Masking")
        st.dataframe(df_masked.head())

        output = io.BytesIO()
        df_masked.to_csv(output, index=False)
        st.download_button("Download Hasil", output.getvalue(), "masked_output.csv", "text/csv")