# Flights - Data Visualization


<h2>
This project includes basic data visualization methods can be used with python libraries numpy, pandas, matplotlib and seaborn.</h2>
<h3>The data sheet used in this project is a flight detail dataframe about Indian flights and destnations.</h3>
<h5>Screenshots of output tables have included in the below table with corresponding python code.</h5>
<span></span>

<h4>1) Visualizing bar plot of 'Source' column (port of departure) with number of flights from each source in the flights datframe (lets's say df).</h4>

```python 
sb.countplot(data = flights, x= 'Source')
plt.ylabel('Number of flights',fontsize=12)
plt.xlabel('Source',fontsize=12)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>2) Displaying same plot (1)  with minor changes of its appearance. Colors of the bars are changed and the x lables have a rotation of 30 degrees.</h4>

```python 
base_color = sb.color_palette()[0]
sb.countplot(data = flights, x = 'Source', color = base_color)
plt.xticks(rotation = 30)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar2.png" width="350" title="hover text" >
</p> 

<h4>3) Displaying same plot (1)  with appearance changed to orange and the indeces have been ordered to decending order.</h4>

```python 
base_color = sb.color_palette()[1]
gen_order = flights['Source'].value_counts().index
sb.countplot(data = flights, x = 'Source', color = base_color, order = gen_order)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar3.png" width="350" title="hover text" >
</p> 

<h4>4) Visualizing the bar plot of the column 'Airlines' indicating the variety of airline. The x labels have been rotated 90 degrees.</h4>

```python 
base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color)
plt.xticks(rotation = 90);
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar5.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>displaying plot sample</h4>

```python 
s = "Python syntax highlighting"
print s
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 


