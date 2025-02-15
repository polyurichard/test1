import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

import json
video_id = "gAkwW2tuIqE"
transcript_dict = YouTubeTranscriptApi.get_transcript(video_id)
print(json.dumps(transcript_dict, indent=4))

st.write(transcript_dict)
