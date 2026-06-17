"""
Shared data loading for the Ocean Data Finder app.
Keeps the file path and sheet logic in ONE place so the pages stay simple
and nothing is hardcoded to a single machine.
"""
from pathlib import Path
import pandas as pd
import streamlit as st

# Path is relative to THIS file, so it works on any machine and on Streamlit Cloud.
DATA_FILE = Path(__file__).parent / "data" / "Ocean_Open_Data_Finder.xlsx"

GLOBAL_SHEET = "GLOBAL_DATASETS"
INDIAN_OCEAN_SHEET = "INDIAN_OCEAN_DATASETS"


@st.cache_data
def load_data(scope: str = "Global"):
    """scope: 'Global' (all datasets) or 'Indian Ocean' (regional only)."""
    sheet = INDIAN_OCEAN_SHEET if scope == "Indian Ocean" else GLOBAL_SHEET
    df = pd.read_excel(DATA_FILE, sheet_name=sheet)
    # Drop fully-empty rows just in case, and strip whitespace from headers
    df.columns = [c.strip() for c in df.columns]
    return df


def scope_selector(location="sidebar"):
    """Render a Global vs Indian Ocean toggle and return the chosen scope."""
    target = st.sidebar if location == "sidebar" else st
    return target.radio(
        "🌐 Coverage",
        ["Global", "Indian Ocean"],
        help="Global = all datasets. Indian Ocean = regional subset only.",
        horizontal=(location != "sidebar"),
    )
