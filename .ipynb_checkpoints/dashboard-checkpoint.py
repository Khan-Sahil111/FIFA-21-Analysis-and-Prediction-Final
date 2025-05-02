import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from math import pi

st.set_page_config(layout="wide", page_title="FIFA 21 Player Analysis")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("players_21.csv")
    df["dob"] = pd.to_datetime(df["dob"])
    df["joined"] = pd.to_datetime(df["joined"])
    df["born_year"] = df["dob"].dt.year
    df["value_eur"] = df["value_eur"] / 1e6
    df["wage_eur"] = (df["wage_eur"] * 48) / 1e6
    df.rename(columns={"value_eur": "value_eur_m", "wage_eur": "wage_eur_m"}, inplace=True)
    return df

df = load_data()

# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Player Comparison", "Team Analysis", "Distributions"])

# Home Page
if section == "Home":
    st.title("FIFA 21 Player Dataset Dashboard")

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Players", df.shape[0])
    col2.metric("Unique Clubs", df["club_name"].nunique())
    col3.metric("Unique Nations", df["nationality"].nunique())

    st.markdown("### 🏆 Top 5 Most Valuable Players (in €M)")
    top_value = df[['short_name', 'club_name', 'value_eur_m']].sort_values(by='value_eur_m', ascending=False).head(5)
    st.table(top_value.set_index('short_name'))

    st.markdown("### 💰 Top 5 Highest Wage Earners (Annual in €M)")
    top_wage = df[['short_name', 'club_name', 'wage_eur_m']].sort_values(by='wage_eur_m', ascending=False).head(5)
    st.table(top_wage.set_index('short_name'))

    st.markdown("### 🧓 Player Age Distribution")
    fig_age, ax_age = plt.subplots()
    sns.histplot(df["born_year"].apply(lambda x: 2020 - x), bins=20, kde=True, color='teal', ax=ax_age)
    ax_age.set_xlabel("Age")
    st.pyplot(fig_age)

    st.markdown("### ⚽ Value vs. Overall Rating (Bubble Chart)")
    bubble_df = df[df["value_eur_m"] < 100]
    fig_bubble, ax_bubble = plt.subplots()
    bubble = ax_bubble.scatter(
        bubble_df["overall"], 
        bubble_df["value_eur_m"], 
        s=bubble_df["wage_eur_m"] * 10,
        alpha=0.5,
        c='orange',
        edgecolors='k'
    )
    ax_bubble.set_xlabel("Overall Rating")
    ax_bubble.set_ylabel("Value (€M)")
    ax_bubble.set_title("Player Value vs Overall Rating (Bubble size = Wage)")
    st.pyplot(fig_bubble)


# Player Radar Comparison
elif section == "Player Comparison":
    st.title("Player Radar Chart Comparison")
    players = st.multiselect("Choose players", df["short_name"].unique(), default=["L. Messi", "Cristiano Ronaldo"])
    attributes = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']

    for player in players:
        st.subheader(player)
        player_data = df[df['short_name'] == player]
        if not player_data.empty:
            values = player_data[attributes].values.flatten().tolist()
            values += values[:1]
            angles = [n / float(len(attributes)) * 2 * pi for n in range(len(attributes))]
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.plot(angles, values, linewidth=2)
            ax.fill(angles, values, alpha=0.3)
            plt.xticks(angles[:-1], attributes)
            st.pyplot(fig)
        else:
            st.warning(f"{player} not found in the dataset.")

# Team Analysis
elif section == "Team Analysis":
    st.title("Team-Based Metric Distribution")
    country = st.selectbox("Select Country", df["nationality"].unique())
    team_df = df[df["nationality"] == country]
    st.subheader(f"Players from {country}")
    st.dataframe(team_df[["short_name", "overall", "potential", "value_eur_m", "pace", "shooting", "passing"]].head(10))

    st.subheader("Metric Distributions")
    selected_metric = st.selectbox("Choose a metric", ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic'])
    fig, ax = plt.subplots()
    sns.histplot(team_df[selected_metric], bins=15, kde=True, ax=ax)
    st.pyplot(fig)

# Feature Distributions
elif section == "Distributions":
    st.title("Feature Distributions")
    selected = st.selectbox("Choose a numeric feature", df.select_dtypes(include=np.number).columns)
    fig1, ax1 = plt.subplots()
    sns.histplot(df[selected], kde=True, ax=ax1)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    sns.boxplot(x=df[selected], ax=ax2)
    st.pyplot(fig2)
