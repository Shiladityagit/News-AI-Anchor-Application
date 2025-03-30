import streamlit as st
import requests
import openai
from news_video import VideoGenerator
from dotenv import load_dotenv
import os
from newsapi import NewsApiClient

load_dotenv()

API_KEY = "103931deb9954669bc3f7d5ac6d620f1"
newsapi = NewsApiClient(api_key=API_KEY)
video_api_key = os.getenv("BEARER_TOKEN")
video_generator = VideoGenerator(video_api_key)

st.set_page_config(page_title="AI News Anchor", layout="wide")

st.title("NEWSIEE")
st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
st.subheader('AUTOMATED NEWS CHANNEL WITH AI NEWS ANCHOR')
st.markdown('<style>h3{color: pink; text-align: center;}</style>', unsafe_allow_html=True)

image_url = "https://i.ibb.co/hYcxXTW/anchor.png"

# User input for query
query = st.text_input("Enter a news topic (e.g., AI, sports, politics):", "").strip()
num_news = st.slider("Number of News", min_value=1, max_value=5, value=3)

if st.button("Generate"):
    if query and num_news > 0:
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.info("Your AI News Anchor: Sophie")
            st.image(image_url, caption="Anchor Image", use_column_width=True)
        
        with col2:
            # Fetch news based on query
            news_articles = newsapi.get_everything(q=query, language="en", sort_by="publishedAt")

            if news_articles and news_articles["totalResults"] > 0:
                st.success(f"News about '{query}'")
                numbered_paragraphs = ""

                # Limit news articles to num_news
                for i, article in enumerate(news_articles["articles"][:num_news], start=1):
                    title = article['title']
                    summary = article['description'] if article['description'] else "No summary available"
                    link = article['url']
                    news_entry = f"{i}. {title} - {summary}\n"
                    st.write(news_entry)
                    numbered_paragraphs += news_entry + "\n"
            else:
                st.error("No articles found! Try a different topic.")
                numbered_paragraphs = ""
        
        with col3:
            final_text = f"""
                Hello World, I'm Sophie, your AI News Anchor. Bringing you the latest updates on {query}.
                Here are the news for you:
                {numbered_paragraphs}
                That's all for today. Stay tuned for more news, Thank you!
            """
            
            if numbered_paragraphs:
                video_url = video_generator.generate_video(final_text, image_url)
                st.warning("AI News Anchor Video")
                st.video(video_url)
    else:
        st.error("Please enter a query and select at least one news item.")
