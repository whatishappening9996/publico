import streamlit as sl
import time

fil = sl.file_uploader(label='Upload an image')
txt = sl.text_input(label='Or copy/paste a med list here')
btn = sl.button(label= 'Analyze')