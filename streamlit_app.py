import streamlit as st

# ===== 背景色（カフェオレ色）をCSSで設定 =====
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f5e6ca; /* カフェオレ色 */
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
h1, h2, h3, p, label {
    color: #5a4632 !important; /* 深いブラウン文字 */
    font-family: "Segoe UI", "Cursive", sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ===== タイトル（筆記体っぽい） =====
st.markdown(
    "<h1 style='text-align: center; font-family: cursive; color: #5a4632;'>☕ Coffee Price Checker</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>どちらのコーヒーがよりお得かをチェックしましょう。</p>", unsafe_allow_html=True)
st.write("")

# ===== Aのコーヒー =====
st.subheader("Aのコーヒー")
a_price = st.number_input("Aの値段（円）", min_value=0, value=0)
a_weight = st.number_input("Aのグラム数（g）", min_value=0, value=0)

# ===== Bのコーヒー =====
st.subheader("Bのコーヒー")
b_price = st.number_input("Bの値段（円）", min_value=0, value=0)
b_weight = st.number_input("Bのグラム数（g）", min_value=0, value=0)

# ===== 結果ボタン =====
if st.button("結果を表示"):
    if a_price == 0 or b_price == 0:
        st.warning("⚠️ 値段が0のままだと計算できません。")
    else:
        a_per_yen = a_weight / a_price
        b_per_yen = b_weight / b_price

        st.markdown(
            f"<p style='font-size: 20px;'>☕ Aの1円あたりの量： <b>{a_per_yen:.3f} g</b></p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size: 20px;'>☕ Bの1円あたりの量： <b>{b_per_yen:.3f} g</b></p>",
            unsafe_allow_html=True
        )

    if a_per_yen > b_per_yen:
        st.markdown(
            "<div style='background-color:#e7d7c1; padding:12px; border-radius:8px; font-size:22px; color:#5a4632;'>"
            "✅ Aのコーヒーの方がお得です！"
            "</div>",
            unsafe_allow_html=True
        )

    elif b_per_yen > a_per_yen:
        st.markdown(
            "<div style='background-color:#e7d7c1; padding:12px; border-radius:8px; font-size:22px; color:#5a4632;'>"
            "✅ Bのコーヒーの方がお得です！"
            "</div>",
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            "<div style='background-color:#e7d7c1; padding:12px; border-radius:8px; font-size:22px; color:#5a4632;'>"
            "🟰 同じ価値です。"
            "</div>",
            unsafe_allow_html=True
        )

