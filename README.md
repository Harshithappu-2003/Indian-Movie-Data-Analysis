# Indian Movie Data Analysis

## Overview
Indian Movie Data Analysis is an interactive web application that provides insights into Indian movies using a dataset. Users can search for movies, apply filters, and generate visualizations to analyze the data effectively. Built with Streamlit and Plotly, this application is user-friendly and highly customizable.

## Features
1. **Search Movies by Name**: 
   - Perform partial or full-name searches.
   - Results are displayed dynamically in a table format.

2. **Filters**: 
   - **Genre**: Filter movies by genre.
   - **Year**: Specify a year range using a slider.
   - **Language**: Filter movies based on language.
   - **Rating**: (Planned slider integration for future enhancement.)
   - **Votes**: (Planned slider integration for future enhancement.)

3. **Visualizations**:
   - **Top 10 Movies by Ratings**: Display the top-rated movies with a bar chart visualization.
   - **Top 10 Movies by Votes**: Show the most-voted movies with a bar chart visualization.
   - **Upcoming Visualizations**:
     - Rating distribution.
     - Votes vs. Ratings.
     - Top genres by count.

4. **Data Display**:
   - View the entire dataset or filtered results in a table format.
   - Includes details such as movie name, year, duration, rating, votes, genre, and language.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the interactive web app.
- **Plotly**: For creating interactive visualizations.
- **Pandas**: For dataset manipulation and analysis.
- **Matplotlib**: (Optional future visualizations.)

## Installation
Follow the steps below to run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/indian-movie-data-analysis.git

   # Indian Movie Data Analysis

## Dataset

The dataset `output.csv` must be placed in the **root directory** of the project. It includes the following columns:

- **Movie Name**: The name of the movie.
- **Year**: The year of release.
- **Timing (min)**: The duration of the movie in minutes.
- **Rating (10)**: The rating of the movie out of 10.
- **Votes**: The number of votes the movie has received.
- **Genre**: The genre of the movie.
- **Language**: The language in which the movie was made.

## How to Use

1. **Launch the App**  
   To launch the app, run the following command in your terminal:
   ```bash
   streamlit run app.py

## Screenshot
![Screenshot 2025-01-09 223257](https://github.com/user-attachments/assets/1ea50011-a31b-4b87-acfb-f39db822c900)
