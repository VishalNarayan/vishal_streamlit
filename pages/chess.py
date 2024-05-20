import streamlit as st
import streamlit.components.v1 as components

icon_url = "https://cdn3.emoji.gg/emojis/8073-brilliant.png"
st.set_page_config(page_icon=icon_url)
# Custom CSS for responsiveness
st.markdown("""
    <style>
    /* Adjust the iframe size for different screen widths */
    @media (max-width: 600px) {
        iframe {
            width: 80% !important;
            height: 600px !important;
        }
    }
    @media (min-width: 601px) and (max-width: 1200px) {
        iframe {
            width: 80% !important;
            height: 600px !important;
        }
    }
    @media (min-width: 1201px) {
        iframe {
            width: 800px !important;
            height: 600px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Function to replace :brilliant: with the HTML image tag
def replace_brilliant_with_icon(text):
    icon_html = f'<img src="{icon_url}" width="20" style="vertical-align: middle;">'
    return text.replace(":brilliant:", icon_html)


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
# Embed the chess game or board in a responsive container
st.markdown(f"""
    <div class="iframe-container">
        <iframe class="responsive-iframe" src="{game_url}" allowfullscreen></iframe>      
    </div>
    """, unsafe_allow_html=True)