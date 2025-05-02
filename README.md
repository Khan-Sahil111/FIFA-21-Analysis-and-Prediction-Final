# FIFA 21 Player Data Analysis: A Comprehensive Exploration Using Python and Streamlit

## 📄 Abstract
The increasing availability of data in the world of football has revolutionized how players are evaluated, teams are formed, and strategies are developed. This study presents an in-depth analysis of the FIFA 21 player dataset using a combination of Python-based analytical tools and Streamlit for creating an interactive web application.

The objective is to transform raw player statistics into meaningful visual insights that can support data-driven decisions for scouts, analysts, and fans. Our approach includes preprocessing of the data, exploratory data analysis (EDA), and the development of a feature-rich dashboard. The dashboard is divided into various sections such as Home, Player Comparison, Team Analysis, and Feature Distributions. It highlights player market value, wage structure, performance attributes, and national trends.

This paper elaborates on each of these sections, discussing the methodology, visual outputs, and the analytical value they offer. We conclude by outlining future work and potential improvements.

---

## 1. 📌 Introduction
Data analytics has transformed many domains, and professional football is no exception. From scouting talent to optimizing player performance and developing game strategies, the insights derived from data play a vital role.

The **FIFA 21 video game dataset** is an excellent proxy for real-world player statistics. Though simulated, it closely mirrors real-life assessments and valuations of players across various leagues and countries. This study analyzes over **18,000 football players** using statistical and visualization techniques.

The primary goal is to convert a high-dimensional dataset into interactive, digestible insights through a **Streamlit dashboard**, making evaluation accessible to both data scientists and football enthusiasts.

---

## 2. 📊 Dataset Overview

### Included Variables:
- **Personal Info**: Name, DOB, nationality, club, preferred foot.
- **Performance Metrics**: Pace, shooting, passing, dribbling, defending, physical.
- **Market Metrics**: Overall rating, potential, market value (€), weekly wage (€).
- **Goalkeeping Attributes**: Diving, reflexes, handling, etc.

### 2.1 Data Preprocessing
- Converted `dob` and `joined` columns to `datetime`.
- Calculated player age as of 2020.
- Normalized `value_eur` and `wage_eur` to millions for readability.
- Cleaned and standardized column names.

---

## 3. 🛠 Methodology

### 3.1 Tools & Technologies
- **Python** – Core programming language.
- **pandas** – Data loading and manipulation.
- **seaborn & matplotlib** – Visualizations.
- **Streamlit** – Web dashboard creation.

### 3.2 Dashboard Architecture

#### 🏠 Home Page
- Summary metrics, top-valued players, wage earners, age distribution, and bubble chart (value vs. rating).

#### 🔄 Player Comparison
- Radar charts comparing selected players across six core metrics.

#### 🌍 Team Analysis
- Filters players by nationality.
- Shows top 10 players and distribution of selected metrics.

#### 📈 Distributions
- Histogram and boxplot of selected numerical features to explore spread, skewness, and outliers.

---

## 4. 📈 Results and Analysis

### 4.1 Home Section
- **Total Players**: ~18,000  
- **Unique Clubs**: 698  
- **Unique Nations**: 150+

#### Top 5 Most Valuable Players:
- Includes Messi, Ronaldo, Neymar.

#### Top 5 Wage Earners:
- Highlights market disparities in wages.

#### Age Distribution:
- Right-skewed; majority aged 20–28.

#### Bubble Chart (Overall vs. Value):
- Bubble size = wage.  
- Positive correlation between rating and value.

---

### 4.2 Player Radar Comparison
Compare players based on:
- **Pace**, **Shooting**, **Passing**, **Dribbling**, **Defending**, **Physic**

Example:
- *Messi*: High dribbling & passing  
- *Ronaldo*: Strong in shooting & physicality

Useful for identifying tactical compatibility.

---

### 4.3 Team Analysis Section
- Select a country to filter and analyze players.
- Shows:
  - Top 10 by rating/value.
  - Histogram of a selected metric (e.g., pace of Brazilian players).

Helps reveal national strengths:
- African countries: Physical players  
- Spain: High passing ability

---

### 4.4 Distributions Section
- Visualize any numeric feature:
  - Histogram for spread/skewness.
  - Boxplot for medians and outliers.

Examples:
- Wage disparity (few high earners)
- Skill variance across positions

---

## 5. 💬 Discussion

### Key Insights:
- Moderate correlation between player value and performance.
- Skewed wage distribution – few elite earners.
- Clear national patterns in skill attributes.
- Radar comparisons enhance tactical decision-making.

### 5.1 Limitations:
- Simulated data (FIFA) vs. real-world stats.
- No dynamic match data included.
- Goalkeepers and outfield players analyzed together.
- Time-bound to 2020 only.

---

## 6. ✅ Conclusion
This project demonstrates the synergy between data analysis and interactive web tools in sports analytics. Despite being synthetic, the FIFA 21 dataset reveals patterns in player attributes, market valuation, and national trends.

The dashboard is designed to serve a wide range of users – from casual fans to professional scouts – and highlights the importance of visual storytelling in analytics.

---

## 7. 🔮 Future Work
- **Time-Series Analysis**: Track player growth across FIFA editions.
- **Real Data Integration**: Compare with platforms like Transfermarkt.
- **Role-Specific Models**: Separate models for different positions.
- **Custom Upload**: Allow user-submitted data for analysis.

---

## 8. 📚 References
- EA Sports FIFA 21 Dataset (Kaggle)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Seaborn](https://seaborn.pydata.org/) and [Matplotlib](https://matplotlib.org/) Libraries
- [pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) Documentation
- “Data Science for Soccer” – Soccerment Blog
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

## 📎 Appendix
- **Code**: Available in attached Python and Jupyter Notebook files.
- **Screenshots**: Available upon request.
- **Dataset Description**: CSV column dictionary included.
