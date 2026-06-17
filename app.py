import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from data_loader import load_data

st.set_page_config(page_title="Ocean Data Finder", layout="wide")

st.title("🌊 Ocean Data Finder")

st.markdown("""
### Find ocean datasets instantly

This tool helps early-career researchers quickly discover open ocean datasets
by variable, region, skill level, and more.

👉 Use the sidebar to navigate:
- 🔍 **Search** datasets
- 📊 **Browse** all datasets
- ℹ️ **About** this project
""")

# --- Live counts so the homepage reflects the real data ---
try:
    g = load_data("Global")
    io = load_data("Indian Ocean")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total datasets", len(g))
    c2.metric("Indian Ocean datasets", len(io))
    c3.metric("Variables covered", g["Variable"].nunique())
except Exception as e:
    st.warning(f"Could not load dataset counts: {e}")

st.success("Start by clicking 'Search' in the sidebar 🚀")
