"""
Name: Mark Guerra
CS230: Section SN2F
Data: Volcanoes
URL:

Description:
"""

import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import base64

main_bg = "Vbg.jpg"
main_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

df = pd.read_csv("volcanoes.csv")
# print(df["Country"])

countries =[]
for country in df["Country"]:
    if country not in countries:
        countries.append(country)

countries = sorted(countries)
st.title("Volcanoes of the World")
from PIL import Image
img = Image.open("cartoon volcano.jpg")
st.image(img, width=400)

select_country = st.selectbox("Select a country: ", countries)
st.write(select_country)

volcano_names = []
for name in df["Volcano Name"]:
    volcano_names.append(name)
# st.write(volcano_names)

country_names = []
for name in df["Country"]:
    country_names.append(name)
# st.write(country_names)

data_set = list(zip(country_names, volcano_names))

latitude = []
for lat in df["Latitude"]:
    latitude.append(lat)

longitude = []
for long in df["Longitude"]:
    longitude.append(long)

coordinates = list(zip(volcano_names, latitude, longitude))
volcano_coordinates = {}
for location in coordinates:
    volcano_coordinates[location[0]] = location[1], location[2]


# st.write(data_set)

# counties_volcanoes = {}
# for value in data_set:
#     volcanoes = []
#     if value[0] not in counties_volcanoes:
#         counties_volcanoes[value[0]] = value[1]
#     else:
#         counties_volcanoes[value[0]] += value[1]
# st.write(counties_volcanoes)

countries_volcanoes = {}
for key1 in data_set:
    volcanoes = []
    for key2 in data_set:
        if key1[0] == key2[0]:
            volcanoes.append(key2[1])
        countries_volcanoes[key1[0]] = volcanoes
# st.write(countries_volcanoes)

# for volcano in select_country:
#     st.write(counties_volcanoes[select_country])

# st.write(countries_volcanoes[select_country])
count = len(countries_volcanoes[select_country])
st.write(f"There are", count,  "volcanoes in", select_country)

st.write(f"Map of Volcanoes in", select_country)
country_coords = []
for volcano in countries_volcanoes[select_country]:
    if volcano in volcano_coordinates:
        individual_coord = []
        lat = volcano_coordinates[volcano][0]
        lon = volcano_coordinates[volcano][1]
        individual_coord.append(volcano)
        individual_coord.append(lat)
        individual_coord.append(lon)
        country_coords.append(individual_coord)
        # st.write(individual_coord)
        # data = list(zip(str(volcano), lat, lon))
        # st.write(data)
# st.write(country_coords)
df_map = pd.DataFrame(country_coords, columns=["Volcano", "lat", "lon"])
st.map(df_map)

# def elevation_hist():
#     elevation = []
#     for height in df["Elevation"]:
#         elevation.append(height)
#     volcano_elevation = list(zip(volcano_names, elevation))
#     return volcano_elevation
# elevation_hist()

elevation = []
for height in df["Elevation (m)"]:
    elevation.append(height)

subregion = []
for region in df["Subregion"]:
    subregion.append(region)

regions = []
for region in df["Region"]:
    regions.append(region)

region_elevation = list(zip(regions, elevation))

subregion_elevation = list(zip(subregion, elevation))
# st.write(subregion_elevation)

regions_sorted = []
for region in df["Region"]:
    if region not in regions_sorted:
        regions_sorted.append(region)
regions_sorted = sorted((regions_sorted))

regions_with_elevations = {}
for key1 in region_elevation:
    elevations = []
    for key2 in region_elevation:
        if key1[0] == key2[0]:
            elevations.append(key2[1])
        regions_with_elevations[key1[0]] = elevations

subregion_sorted = []
for subregion in df["Subregion"]:
    if subregion not in subregion_sorted:
        subregion_sorted.append((subregion))
subregion_sorted = sorted(subregion_sorted)

subregion_with_elevations = {}
for key1 in subregion_elevation:
    elevations = []
    for key2 in subregion_elevation:
        if key1[0] == key2[0]:
            elevations.append(key2[1])
        subregion_with_elevations[key1[0]] = elevations

# st.write(subregion_with_elevations)
# select_subregion = st.selectbox("Select a subregion:", subregion_sorted)
# st.write("\n")
# def histogram():
#     fig, ax = plt.subplots()
#     x = subregion_with_elevations[select_subregion]
#     ax.hist(x, bins=[-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], color="orangered")
#     ax.set_title(f"Histogram of Volcano Elevations: {select_subregion}", color= "crimson")
#     ax.set_xlabel("Elevation (meters)", color= "navy")
#     ax.set_ylabel("# of Volcanoes", color= "navy")
#     ax.grid(which="both")
#     ax.grid(color="sienna", linestyle="--")
#     ax.set_facecolor("wheat")
#     st.pyplot(fig)
#
# histogram()
select_region = st.selectbox("Select a region:", regions_sorted)
st.write("\n")
def histogram():
    fig, ax = plt.subplots()
    x = regions_with_elevations[select_region]
    ax.hist(x, bins=[-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], color="orangered")
    ax.set_title(f"Histogram of Volcano Elevations: {select_region}", color= "crimson")
    ax.set_xlabel("Elevation (meters)", color= "navy")
    ax.set_ylabel("# of Volcanoes", color= "navy")
    ax.grid(which="both")
    ax.grid(color="sienna", linestyle="--")
    ax.set_facecolor("wheat")
    st.pyplot(fig)

histogram()



activity = []
for level in df["Activity Evidence"]:
    activity.append((level))

activity_evidence = []
for level in df["Activity Evidence"]:
    if level not in activity_evidence:
        activity_evidence.append(level)
# st.write(activity_evidence)

activity_evidence_count = []
for evidence in activity_evidence:
    count = activity.count(evidence)
    activity_evidence_count.append(count)
# st.write(activity_evidence_count)

activity_and_count= {}
activitycount = list(zip(activity_evidence, activity_evidence_count))
# st.write(activitycount)
for value in activitycount:
    activity_and_count[value[0]] = value[1]
# st.write(activity_and_count)

st.write("\n")
def pie_chart():
    labels = activity_evidence
    data = activity_evidence_count
    fig, ax = plt.subplots()
    ax.set_title("Pie Chart for Activity Evidence", color='navy')
    ax.axis("equal")
    ax.pie(data, explode=(0, 0, .1, 0, 0, 0, 0), shadow=True, startangle=90, colors=["darkblue", "teal", "crimson", "coral", "darkgreen", "lightgreen", "salmon"])
    plt.legend(labels, loc=0)
    st.pyplot(fig)

# pie_chart()

# x = st.slider('Guess how many volcanoes there are in the world',0, 2000, 10)
# if x == 1413:
#     st.write("Correct! There are 1,413 Volcanoes in the World.")
# elif (x - 1413) <= 100 and (x - 1413) >= -100:
#     st.write("Close! Try again.")
# elif (x - 1413) <= 10 and (x - 1413) >= -10:
#     st.write("So Close! Try again.")
# else:
#     st.write("Oops! Not Close Enough. Try again.")

options = ["Pie Chart", "Guessing Game"]
chart = st.radio("Pie chart for activity evidence or guess the number of volcanoes in the world?", options)
if chart == "Pie Chart":
    pie_chart()
else:
    x = st.slider('Guess how many volcanoes there are in the world',0, 2000, 10)
    if x == 1413:
        st.write("Correct! There are 1,413 Volcanoes in the World.")
    elif (x - 1413) <= 50 and (x - 1413) >= -50:
        st.write("Good Guess! There are 1,413 Volcanoes in the World.")
    else:
        st.write("Not Close Enough. Try again.")

st.write("Thank You for visiting. Come again!")
