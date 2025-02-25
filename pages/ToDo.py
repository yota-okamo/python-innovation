import streamlit as st
import pickle
import os

st.title("TODOリスト")

# 保存ファイル名
SAVE_FILE = "todo.txt"

# データの読み込み
def load_file():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            return pickle.load(f)
    return []

# データの書き込み
def save_file(value):
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(value, f)

# タスクリストの初期化
if "tasks" not in st.session_state:
    st.session_state.tasks = load_file()

# 新規タスク追加
new_task = st.text_input("タスクを入力")
if st.button("追加"):
    if new_task:
        st.session_state.tasks.append(new_task)
        save_file(st.session_state.tasks)
        st.experimental_rerun()

# タスク一覧表示
st.subheader("タスク一覧")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(task)
    if col2.button("削除", key=i):
        # st.session_state.pop(i)
        del st.session_state["tasks"][i]
        save_file(st.session_state.tasks)
        st.experimental_rerun()