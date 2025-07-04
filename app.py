import streamlit as st
import pandas as pd
from utils import mask_name, mask_email, mask_phone, mask_address, mask_purchase_id, mask_birthdate, mask_socialmedia, mask_age
import io

st.title("PII Masker")

uploaded_file = st.file_uploader("Unggah file", type=["csv", "xls", "xlsx"])

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
            'Full Name': mask_name,
            'Customer Name': mask_name,
            'User Name': mask_name,
            'Customer Name' : mask_name,
            'Nama': mask_name,
            'Surname': mask_name,
            'Nama Lengkap': mask_name,
            'Email': mask_email,
            'Email Address': mask_email,
            'Customer Email': mask_email,
            'Alamat Email': mask_email,
            'Phone': mask_phone,
            'Phone Number': mask_phone,
            'Contact Number': mask_phone,
            'Mobile': mask_phone,
            'Mobile Number': mask_phone,
            'Telepon': mask_phone,
            'Nomor Telepon': mask_phone,
            'HP': mask_phone,
            'No. HP': mask_phone,
            'Address': mask_address,
            'Home Address': mask_address,
            'Shipping Address': mask_address,
            'Billing Address': mask_address,
            'Alamat': mask_address,
            'Alamat Lengkap': mask_address,
            'Alamat Pengiriman': mask_address,
            'Alamat Penagihan': mask_address,
            'Birthdate': mask_birthdate,
            'Tanggal Lahir': mask_birthdate,
            'Tahun Lahir': mask_birthdate,
            'Born Date': mask_birthdate,
            'Date of Birth': mask_birthdate,
            'Social Media': mask_socialmedia,
            'Instagram': mask_socialmedia,
            'Instagram Username': mask_socialmedia,
            'Instagram ID': mask_socialmedia,
            'X': mask_socialmedia,
            'X Username': mask_socialmedia,
            'X ID': mask_socialmedia,
            'Tiktok': mask_socialmedia,
            'Tiktok Username': mask_socialmedia,
            'Tiktok ID': mask_socialmedia,
            'Umur': mask_age,
            'Age': mask_age
        }

        columns_to_mask_only = {
            'PurchaseID': mask_purchase_id,
            'Transaction ID': mask_purchase_id,
            'Order ID': mask_purchase_id,
            'ID Pembelian': mask_purchase_id,
            'ID Transaksi': mask_purchase_id,
            'ID Pesanan': mask_purchase_id
        }

        new_columns = []
        for col in df_masked.columns:
            if col in columns_to_mask_and_suffix:
                mask_function = columns_to_mask_and_suffix[col]
                df_masked[col] = df_masked[col].astype(str).apply(mask_function)
                new_columns.append(f"{col}_PII")
            elif col in columns_to_mask_only:
                mask_function = columns_to_mask_only[col]
                df_masked[col] = df_masked[col].astype(str).apply(mask_function)
                new_columns.append(col)
            else:
                new_columns.append(col)

        df_masked.columns = new_columns

        st.subheader("Hasil Dataset Setelah Masking")
        st.dataframe(df_masked.head())

        output = io.BytesIO()
        df_masked.to_csv(output, index=False)
        st.download_button("Download Hasil", output.getvalue(), "masked_output.csv", "text/csv")
