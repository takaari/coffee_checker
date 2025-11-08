import streamlit as st

st.title("☕ コーヒーお得度チェッカー")

st.write("2つのコーヒーについて、1円あたりに買えるグラム数を比較します。")

# Aの情報入力
st.subheader("Aのコーヒー")
a_price = st.number_input("Aの値段（円）", min_value=1)
a_weight = st.number_input("Aのグラム数（g）", min_value=1)

# Bの情報入力
st.subheader("Bのコーヒー")
b_price = st.number_input("Bの値段（円）", min_value=1)
b_weight = st.number_input("Bのグラム数（g）", min_value=1)

if st.button("結果を表示"):
    a_per_yen = a_weight / a_price
    b_per_yen = b_weight / b_price

    st.write(f"☕ Aの1円あたりの量：**{a_per_yen:.3f} g**")
    st.write(f"☕ Bの1円あたりの量：**{b_per_yen:.3f} g**")

    if a_per_yen > b_per_yen:
        st.success("✅ Aのコーヒーの方がお得です！")
    elif b_per_yen > a_per_yen:
        st.success("✅ Bのコーヒーの方がお得です！")
    else:
        st.info("🟰 同じ価値です。")
