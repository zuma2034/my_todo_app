import streamlit as st
import functions


todos = functions.open_file()
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_file(todos)


st.title("My to do app")
st.subheader("subheader")
st.write("this is my first web")

for index,todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add a new todo",
              on_change = add_todo , key = "new_todo")
print("hello")


st.session_state