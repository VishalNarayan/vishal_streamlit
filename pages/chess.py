import streamlit as st

icon_url = "https://cdn3.emoji.gg/emojis/8073-brilliant.png"

# Function to replace :brilliant: with the HTML image tag
def replace_brilliant_with_icon(text):
    icon_html = f'<img src="{icon_url}" width="20" style="vertical-align: middle;">'
    return text.replace(":brilliant:", icon_html)

st.set_page_config(page_icon=icon_url)
st.title("My Chess Journey")

st.write('''
Over time, I will populate this page with various items, including:
- Educational / Significant games (played by me or others)
- Opening lines and explanations
- Common tactical motifs 
- Unique positions
- A sparsely documented account of my progress as I grow and develop my chess skills
''')

text = replace_brilliant_with_icon(f"For now, here is a game I am particularly proud of. `15..Rxc3` was considered a brilliant :brilliant: move by the chess.com engine. See if you can understand why!")
st.write(text, unsafe_allow_html=True)
game_url = "https://www.chess.com/emboard?id=11828039"
st.components.v1.iframe(game_url, height=600, width=800)
