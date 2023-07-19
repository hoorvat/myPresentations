import plotly as px

# using the iris dataset
df = px.data.iris()

# plotting the bar chart
fig = px.offline.plot(df, x="sepal_width", y="sepal_length", output_type="div")
# fig.write_html("./file.html")
# showing the plot
fig.show()
