import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
import folium

df = pd.read_excel("stolpersteine_DAN_HAG.xlsx")

# מייצר דו"ח EDA מקיף ואוטומטי על הנתונים
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="stolperseine_DAN_HAG", explorative=True)
profile.to_file("stolperseine_DAN_HAG.html")

# --- שלב 1: ניקוי הנתונים ---
# השלמת ערכים חסרים בעמודות ספציפיות על ידי מילוי בערך 'Unknown'
df['NEIGHBOURHOOD'].fillna('Unknown', inplace=True)
df['DISTRICT.1'].fillna('Unknown', inplace=True)

# השמטת שורות שיש בהן חוסרים בעמודות הרלוונטיות
columns_to_check = ['DIRECTION', 'BWT_NUMMER', 'YEAR_PLACEMENT']
df.dropna(subset=columns_to_check, inplace=True)

# השמטת עמודות עם הרבה ערכים חסרים
df.drop(columns=['DESCRIPTION', 'TEXT_ON_THE_STONE'], inplace=True)

print("מספר השורות אחרי הניקוי:", len(df))
print("עמודות אחרי הניקוי:", df.columns.tolist())

coords = df[['LONG', 'LAT']]

inertia = []
K_range = range(1, 15)  # Let's check a range of K from 1 to 14

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(coords)
    inertia.append(kmeans.inertia_)

# --- שלב 2: ניתוח המרפק (Elbow Method) ---

plt.figure(figsize=(10, 6))
plt.plot(K_range, inertia, marker='o', linestyle='--')
plt.title('שיטת המרפק לבחירת K אופטימלי', fontsize=16)
plt.xlabel('מספר המקבצים (K)', fontsize=12)
plt.ylabel('Inertia (סכום ריבועי המרחקים)', fontsize=12)
plt.xticks(K_range)
plt.grid(True)
plt.show()
plt.savefig('elbow_method_plot.png')
print("תרשים המרפק נשמר לקובץ 'elbow_method_plot.png'.")



print("Inertia values:", inertia)
coords = df[['LONG', 'LAT']]

# --- שלב 2: ניתוח המרפק (Elbow Method) ---

# מריץ את K-Means עם K=4 אחרי שראיתי שזה הK האופטימלי
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
df['cluster_kmeans'] = kmeans.fit_predict(coords)

# מוסיף את מרכזי המקבצים (Centroids)
centroids = kmeans.cluster_centers_

# Create the map
# We'll center the map based on the average coordinates
map_center = [coords['LAT'].mean(), coords['LONG'].mean()]
stolpersteine_map = folium.Map(location=map_center, zoom_start=13)

# Define a color palette for the clusters
colors = ['blue', 'red', 'green', 'purple']

# Loop through each row in the DataFrame to add a marker to the map
for index, row in df.iterrows():
    # Access the correct cluster column name: 'cluster_kmeans'
    cluster_color = colors[row['cluster_kmeans']]
    folium.CircleMarker(
        location=[row['LAT'], row['LONG']],
        radius=5,
        color=cluster_color,
        fill=True,
        fill_color=cluster_color,
        fill_opacity=0.7,
        tooltip=f"Cluster: {row['cluster_kmeans']}"
    ).add_to(stolpersteine_map)

# Save the map to an HTML file
stolpersteine_map.save("stolpersteine_clusters_map.html")
