import json
import uuid
from medisearch_client import MediSearchClient
from st_social_media_links import SocialMediaIcons
import streamlit as st
social_media_links = [
    
    "https://www.linkedin.comin/mhmumer/",
    "https://www.github.com/mhmumer/",
]
social_media_icons = SocialMediaIcons(social_media_links)
with st.sidebar:
   api_key = st.text_input("Enter your MediSearch API Key", type="password")
   st.link_button("Create your API Key", "https://medisearch.io/developers/admin?panel=keys")
   st.warning("Made By Muhammad Umer.")
   social_media_icons.render()
   # Create Radio Buttons
   
   
st.title("👨🏼‍⚕️DocAI🤖Powered by MediSearch🩺")

if api_key:
   Query = st.text_area("Enter your Query... ") 
else:
   st.warning("Open the sidebar and enter your  MediSearch API Key")

conversation_id = str(uuid.uuid4())
client = MediSearchClient(api_key=api_key)

if api_key:
   if st.button("Generate Response",type='primary'):
      if Query:
         responses = client.send_user_message(conversation=[Query],
                                             conversation_id=conversation_id,
                                             language="English",
                                             should_stream_response=False)
         print(responses)
         resp=responses[0]
         res=resp.get('text')
         st.info(res)
