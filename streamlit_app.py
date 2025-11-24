import streamlit as st

# ===== ページ全体の背景色を設定（CSS） =====
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f5e6ca; /* カフェオレ色 */
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown("""
    <style>
        label, .st-bx, .st-c5, .st-c4 {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# ===== タイトル =====
st.markdown("<h2 style='text-align: center; color: #5a4632;'>☕ 珈琲お得度比較 ☕</h2>", unsafe_allow_html=True)
st.write("")

st.markdown("<p style='color: #5a4632;'>2つのコーヒーについて、1円あたりに買えるグラム数を比較します。</p>", unsafe_allow_html=True)

# ===== Aの情報入力 =====
st.subheader("Aのコーヒー")
a_price = st.number_input("Aの値段（円）", min_value=0, value=0)
a_weight = st.number_input("Aのグラム数（g）", min_value=0, value=0)

# ===== Bの情報入力 =====
st.subheader("Bのコーヒー")
b_price = st.number_input("Bの値段（円）", min_value=0, value=0)
b_weight = st.number_input("Bのグラム数（g）", min_value=0, value=0)

# ===== 結果表示 =====
if st.button("結果を表示"):
    if a_price == 0 or b_price == 0:
        st.warning("⚠️ 値段が0のままだと計算できません。")
    else:
        a_per_yen = a_weight / a_price
        b_per_yen = b_weight / b_price

        st.markdown(f"<p style='color:#5a4632;'>☕ Aの1円あたりの量：<b>{a_per_yen:.3f} g</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#5a4632;'>☕ Bの1円あたりの量：<b>{b_per_yen:.3f} g</b></p>", unsafe_allow_html=True)

        if a_per_yen > b_per_yen:
            st.success("✅ Aのコーヒーの方がお得です！")
        elif b_per_yen > a_per_yen:
            st.success("✅ Bのコーヒーの方がお得です！")
        else:
            st.info("🟰 同じ価値です。")
