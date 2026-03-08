import streamlit as st
from generator import generate_fake_headline, generate_ai_headline
from scraper import get_trending_news

st.set_page_config(
    page_title="AI Fake News Generator",
    page_icon="📰",
    layout="wide"
)

# -------- MODERN CSS --------

st.markdown("""
<style>

.main-title{
font-size:85px;
font-weight:900;
text-align:center;
background: linear-gradient(90deg,#ff4b4b,#ff9a3c,#ffd93d);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
letter-spacing:1px;
}

.subtitle{
text-align:center;
font-size:24px;
color:#cfcfcf;
margin-bottom:50px;
}

.headline-card{
background:linear-gradient(135deg,#1f2937,#111827);
padding:35px;
border-radius:20px;
font-size:24px;
color:white;
font-weight:600;
box-shadow:0 10px 30px rgba(0,0,0,0.5);
}
            
.news-card{
background:#111827;
padding:15px;
border-radius:15px;
box-shadow:0 8px 25px rgba(0,0,0,0.5);
transition:0.3s;
}

.news-card:hover{
transform:scale(1.03);
}

.news-title{
font-size:17px;
font-weight:600;
margin-top:10px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------- TITLE --------
st.markdown(
"""
<h1 style="
text-align:center;
font-size:100px;
font-weight:800;
background: linear-gradient(90deg,#ff4b4b,#ff9a3c,#ffd93d);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom:5px;
">
🚨 Fake News AI Generator
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p style="
text-align:center;
font-size:32px;
color:#cfcfcf;
margin-bottom:60px;
">
Generate hilarious AI-powered fake headlines
</p>
""",
unsafe_allow_html=True
)

# -------- SIDEBAR --------

st.sidebar.title("⚙️ Features")

feature = st.sidebar.radio(
"",
[
"🎲 Random Fake Headline",
"🤖 AI Headline Generator",
"🌍 Trending News"
]
)

# -------- RANDOM HEADLINE --------

if feature == "🎲 Random Fake Headline":

    st.header("🎲 Random Fake News")

    if st.button("Generate Headline"):

        headline = generate_fake_headline()

        st.markdown(
        f"""
        <div class="headline-card">
        📰 {headline}
        </div>
        """,
        unsafe_allow_html=True
        )

        st.button("📋 Copy Headline")

# -------- AI HEADLINE --------

elif feature == "🤖 AI Headline Generator":

    st.header("🤖 AI Fake Headline Generator")

    topic = st.text_input("Enter Topic")

    if st.button("Generate AI Headline"):

        headline = generate_ai_headline(topic)

        st.markdown(
        f"""
        <div class="headline-card">
        🔥 {headline}
        </div>
        """,
        unsafe_allow_html=True
        )

# -------- TRENDING NEWS --------

elif feature == "🌍 Trending News":

    st.header("🌍 Trending News")

    if st.button("🔄 Refresh News"):
        st.rerun()

    news = get_trending_news()

    col1, col2, col3 = st.columns(3)

    for i, article in enumerate(news):

        col = [col1,col2,col3][i%3]

        with col:

            st.markdown(
            f"""
            <div class="news-card">

            <img src="{article['image']}" width="100%" style="border-radius:10px">

            <div class="news-title">
            {article['title']}
            </div>

            <br>

            <a href="{article['link']}" target="_blank">
            Read Full Article →
            </a>

            </div>
            """,
            unsafe_allow_html=True
            )