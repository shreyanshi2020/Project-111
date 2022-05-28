import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
data = pd.read_csv("medium_data.csv")
data2 = data["reading_time"]
# figure = ff.create_distplot([data2],["Maths Scores"],show_hist = False)
# figure.show()

mean = st.mean(data2)
stdev = st.stdev(data2)
# print(mean)
# print(stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data2[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

stdev = st.stdev(mean_list)
mean = st.mean(mean_list)
print(stdev)

# fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
# fig.show()

first_std_deviation_start, first_std_deviation_end = mean-stdev, mean+stdev
second_std_deviation_start, second_std_deviation_end = mean-(2*stdev), mean+(2*stdev)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdev), mean+(3*stdev)

# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
# fig.show()

data1 = pd.read_csv("data1.csv")
data1 = data1["Math_score"].tolist()
mean1 = st.mean(data1)
print(mean1)
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.show()

data2 = pd.read_csv("data2.csv")
data2 = data2["Math_score"].tolist()
mean2 = st.mean(data2)
print(mean2)
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean2, mean2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD EXTRA CLASSES"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
# fig.show()

data3 = pd.read_csv("data3.csv")
data3 = data3["Math_score"].tolist()
mean3 = st.mean(data3)
print(mean3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean3, mean3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
