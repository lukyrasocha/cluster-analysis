# K-mean cluster analysis

In this assignment I tried to analyse Airline data using the K- mean cluster method. I found the data
on the website FiveThirtyEight. The data set contains data from years 1985 – 1999 and 2000 – 2014.
I used the more recent one and chose to analyse and display number of incidents in correlation to
the distance each airline flights per week. By doing that I wanted to see if there is a relation between
the distance flown and incidents that occur. I also developed an algorithm that helps to find the right
number of clusters using the elbow method and for this concrete dataset I put the data in 4 clusters.


In the createClusters method I set random centroids and put the data in corresponding clusters,
then I calculate new position of the centroids by calculating the average position of all datapoints in
each clusters, when we have the “final position” of the centroids, therefore final clusters I calculate
the distances of the datapoints in the cluster from the centroid. I put this whole process in a for loop
for different number of clusters so eventually I could see what is an ideal number of clusters.
In the findBestK method is where the elbow method happens. I calculate the difference between
each of the distances that are next to each other so I could see where the graph drops most
dramatically. After that I put the differences in a new list and calculated the sum of all the
differences. Then I calculate the relative number by dividing each of the differences by the entire
sum of the differences and I put the results in a new list. Then using if statement I just chose the
relative numbers that are less than 0.15 (so where the graph’s decline is not large) I choose the FIRST
one of them – because that is probably where is the elbow. Then I find to what K cluster does the
first relative number that is smaller than 0.15 belongs to and in clusterList that contains all the
clusters for all of K I choose the right one that I found (the lists are parallel).
In the visualize method I display the datapoints and create nice colours for each of the clusters
