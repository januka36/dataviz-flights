import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

%matplotlib inline

flights = pd.read_csv('C:\Users\Januka Fernando\Desktop\Data Visualization Project\Notebook\flights_data.csv')
print(flights.shape)
flights.head()

######Bar Graph########

#Normal plotting of the 'Source' Column
sb.countplot(data = flights, x= 'Source')
plt.ylabel('Number of flights',fontsize=12)
plt.xlabel('Source',fontsize=12)

#Rotating x label 30 degrees
base_color = sb.color_palette()[0]
sb.countplot(data = flights, x = 'Source', color = base_color)
plt.xticks(rotation = 30)

#Arranging x labels in decreasing order
base_color = sb.color_palette()[1]
gen_order = flights['Source'].value_counts().index
sb.countplot(data = flights, x = 'Source', color = base_color, order = gen_order)

#Plotting 'Airline' column with 90 degree rotation of x labels
base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color)
plt.xticks(rotation = 90);

#Plotting 'Airline' column as y axis
base_color = sb.color_palette()[2]
sb.countplot(data = flights, y = 'Airline', color = base_color)

#Plotting columns with no value_counts
na_counts = flights.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation = 90)
plt.ylabel('Number of missing values', fontsize = 12)


#######Pie Chart########

#Pie chart of the 'Destinantion' column
sorted_counts = flights['Destination'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square')
plt.title('Flight Destination\'s')

#Dough-nut Pie chart of the 'Destinantion' column
sorted_counts = flights['Destination'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square');


#######Histograms######

#Histogram (default) of 'Duration' column
plt.hist(data = flights, x = 'Duration(minutes)')

#Histogram of 'Prize' column with user defined bin number
plt.hist(data = flights, x = 'Price', bins = 20)

#Histogram of 'Prize' column with user defined bin size
bins = np.arange(0, flights['Price'].max()+1, 1200)
plt.hist(data = flights, x = 'Price', bins = bins)
plt.show()

#Histogram of 'price' column with and without kde
sb.distplot(flights['Price']);
sb.distplot(flights['Price'], kde=False);

#Histogram of 'price' column with hist_kws attribute
bin_edges = np.arange(0, flights['Price'].max()+1, 1200)
sb.distplot(flights['Price'], bins = bin_edges, kde = False, hist_kws = {'alpha' : 1});
