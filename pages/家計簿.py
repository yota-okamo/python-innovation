import streamlit as st

# セッション状態を初期化（初回のみ）
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# タイトル
st.title("簡易家計簿アプリ")

choises = ["収入", "支出"]
income = ["お小遣い", "お年玉", "その他"] 
expense = ["ゲーム・書籍", "遊び", "ファッション", "その他"]

# 入力フォーム
st.subheader("収入・支出を記録")
user_choice = st.radio("", choises, horizontal=True)
if user_choice == "収入":
    description = st.selectbox("項目名", income, index=0)
else:
    description = st.selectbox("項目名", expense, index=0)

amount = st.number_input("金額", value=0, step=1000)

if user_choice == "支出":
    amount = -amount

if st.button("追加"):
    if description and amount:
        st.session_state.transactions.append({"項目": description, "金額": amount})
        st.success("追加しました！")
    else:
        st.warning("項目名と金額を入力してください")

# データ表示
st.subheader("履歴")
if st.session_state.transactions:
    total = 0
    for transaction in st.session_state.transactions:
        st.write(f"{transaction['項目']}: {transaction['金額']} 円")
        total += transaction['金額']
    
    st.subheader(f"合計金額: {total} 円")
else:
    st.write("まだ記録がありません。")

# リセットボタン
if st.button("リセット"):
    st.session_state.transactions = []
    st.success("データをリセットしました！")
