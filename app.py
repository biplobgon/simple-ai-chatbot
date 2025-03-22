import streamlit as st
from chatbot import chat_with_bot

st.set_page_config(
    page_title="Gon's Simple AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Gon's Simple AI ChatBot")

st.markdown("""
### Ask me anything!

**Example Questions:**
- What's the capital of France?
- Tell me a joke.
- What's the best way to learn Python?
- How do you stay motivated?

---

*ChatBot made using pre-trained DialoGPT (a HuggingFace transformer model).*

**Developed by - Biplob Gon**  
*Last updated on - 23rd March, 2025*
""")

if 'chat_history_ids' not in st.session_state:
    st.session_state['chat_history_ids'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_input = st.text_input("Your question:", placeholder="Type your question here...")

if st.button("Send 🚀"):
    if user_input.strip():
        response, st.session_state['chat_history_ids'] = chat_with_bot(user_input, st.session_state['chat_history_ids'])
        st.session_state['messages'].append(("You", user_input))
        st.session_state['messages'].append(("Bot", response))

st.markdown("---")
for speaker, message in reversed(st.session_state['messages']):
    if speaker == "You":
        st.markdown(f"🧑‍💻 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")
