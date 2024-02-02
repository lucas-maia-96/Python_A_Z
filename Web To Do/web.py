import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if st.session_state["new_todo"] == "":
        return
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo, label_visibility="visible")
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="asdd", placeholder="Add new todo",
              on_change=add_todo, key="new_todo", label_visibility="collapsed")
