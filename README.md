# Stolpersteine_Exploratory_Clustering
This project performs an exploratory data analysis (EDA) and clustering analysis of Stolpersteine (stumbling stones) data from The Hague, Netherlands.
The primary goal is to uncover hidden geographical patterns by moving beyond administrative boundaries and identifying natural clusters of the stumbling stones. The analysis includes:

- Data Cleaning and EDA: Handling missing values and dropping irrelevant columns.

- Geospatial Clustering: Using the K-Means algorithm to group the stones.

- Visualization: Creating an interactive map to display the results, which reveal four primary concentrations of the project's activity within the city.

About the Stolpersteine Project 🇩🇪
The Stolpersteine (German for "stumbling stones") is a project initiated by German artist Gunter Demnig. It commemorates the victims of the Holocaust and Nazi persecution by placing small, brass plaques in the pavement in front of the victims' last known residences or places of work. Each plaque contains the victim's name, date of birth, date of deportation, and, if known, the date and place of death. The project aims to bring the memory of these individuals back to their everyday environment, making their fate personal and tangible.

The project began in 1996 and has since grown to become the world's largest decentralized monument, with thousands of stones laid across dozens of European countries.

Project Structure 📂
stolpersteine_DAN_HAG.xlsx: The raw dataset containing information about the Stolpersteine in The Hague.

elbow_method_plot.png: The plot generated to determine the optimal number of clusters for the K-Means algorithm.

EDA_Report.html: An automated report detailing the initial data exploration and a summary of the dataset.

stolpersteine_clusters_map.html: An interactive map showcasing the final clustering results, with each cluster color-coded for clarity.

Methodology 💻
The analysis followed a clear two-step methodology:

Data Preparation and EDA: The raw data was loaded, and a comprehensive EDA was performed to understand its structure and identify cleaning needs. Missing values in irrelevant columns were dropped, while important columns were filled with a placeholder value to preserve the dataset's size.

K-Means Clustering: To find the optimal number of clusters, the Elbow Method was used. The analysis identified K=4 as the ideal number of clusters. The K-Means algorithm was then applied to group the Stolpersteine, and the results were visualized on an interactive map.

Results and Conclusion 📈
The analysis successfully identified four distinct geographical clusters of Stolpersteine within The Hague. These clusters do not strictly adhere to administrative boundaries but rather reveal natural concentrations of the memorial project's activity. The interactive map provides a clear visual representation of these clusters, offering new insights into the project's implementation and the historical distribution of the Jewish community in the city.
