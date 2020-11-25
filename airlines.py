# -*- coding: utf-8 -*-
# as inspiration I used the program from the book by Miller & Ranum
import math
import numpy as np
import random
import matplotlib.pyplot as plt
k = [2,3,4,5,6,7,8,9,10,11,12,13,14] # trying different clusters

#Function to calculate the distance of two points

def eucliD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        sum = sum + diff
        distance = math.sqrt(sum)
    return distance
#small comment
#This reads the data file and puts the items we want into a dictionary            
def readAirlineFile(filename):
   with open (filename, "r") as fileHandler: # second argument means "read"
      key = 0
      datadict = {}
      for line in fileHandler:
          key = key + 1
          items = line.split()
          distancePerWeek = float(items[1])
          incidents00_14 = float(items[5])
          datadict[key] = [distancePerWeek,incidents00_14] # adding elements to the dictionary with KEYS and values
   return datadict
# creating initial random centroids and putting all the datapoints to the centroid that are closest to them - creating clusters. After that calculating average position of all datapoints in each clusters and then creating a new centroid based on the average position - after that calculating distances from the centroids again and then putting the datapoints in the clusters.
def createClusters(datadict, repeats):
    clusterList = []
    listOfSum = []  
   
    
    for numberOfClusters in k:
        centroids = [] # creates an empty list
        centroidCount = 0  # starting counting the number of centroids in the list
        centroidKeys = []  # this stores just the indexes of random exam scores stored in datadict
        myMainSum = 0
        while centroidCount < numberOfClusters:     # when we have less centroids than we actually want
            rkey = random.randint(1, len(datadict)) # picks a random key
        
            if rkey not in centroidKeys:    # if the index rkey is not already in the centroidKeys add it to centroidKeys list
                
                centroids.append(datadict[rkey]) # if the condition is fulfilled than add the value stored under the certain key in the dictionary
                centroidKeys.append(rkey) # this adds the rkey to the list so we can check if the rkey has been already used (so we dont pick two points twice)
                centroidCount = centroidCount + 1
        
        for apass in range(repeats):
            
            clusters = [] 
            for i in range(numberOfClusters):
                clusters.append([]) # nested lists = clusters = [[datapoints from cluster1], [datapoints from cluster2], [datapoints from cluster3]......]
            #calculating distances from datapoints to centroids and putting datapoints to corresponding clusters
            for akey in datadict:
                distances = []
                
                for clusterIndex in range(numberOfClusters): 
                    dist = eucliD(datadict[akey], centroids[clusterIndex]) # this calculates the distances (from centroids) to each datapoint
                    distances.append(dist)
                
                mindist = min(distances) # this chooses the minimum distance from the list
                index = distances.index(mindist) # list.indexx finds the element in the list and returns it position
                clusters[index].append(akey)  
                # now when you print clusters[1] you get all the datapoints KEYS that are closest to centroid 1

            dimensions = len(datadict[1]) # how many elements do we have on the first line
            # calculates new centroid for every cluster by calculating the average of the datapoints in corresponding cluster.
            for clusterIndex in range (numberOfClusters):
                sums = [0] * dimensions 
                
                for akey in clusters[clusterIndex]: 
                    datapoints = datadict[akey] # for the fist loop it contains first datapoint from the first cluster
                    for ind in range(len(datapoints)):
                        sums[ind] = sums[ind] + datapoints[ind] # ads up the coordinates so we can calculate the average position of all datapoints in each cluster
                        # sums starts as [0,0] so then we add x coordinates and y coordinates so we get [X SUMS, Y SUMS]
                for ind in range(len(sums)): # in this case is len(sums) = 2
                    clusterLen = len(clusters[clusterIndex])
                    if clusterLen !=0:
                        sums[ind] = sums[ind] / clusterLen # first it divides the sum of x coordinates by the lenght of cluster and then sum of y coordinates by lenght of the cluster
                        
                centroids[clusterIndex] = sums # creates a new centroid that is the average of all datapoints in each cluster
                  
        for clusterIndex in range(numberOfClusters): #calculates the distances
            for akey in clusters[clusterIndex]: # takes all the keys in cluster 1 then in cluster 2 then in cluster....k
                distanceFromCentroid = eucliD(centroids[clusterIndex], datadict[akey])
                myMainSum = myMainSum + distanceFromCentroid
        listOfSum.append(myMainSum)
        indexK = k.index(numberOfClusters)
        clusterList.append([])
        clusterList[indexK].append(clusters)
            
    plt.figure(1)
    plt.plot(listOfSum, '.-')
    plt.show()
    print()
          
    
    return (listOfSum, clusterList)
    
def findBestK(listOfSum, clusterList):
    bestList = []
    best = []
    bestRelative = []
    bestSum = 0
    for index in range(len(listOfSum)-1): 
        bestDifference = listOfSum[index] - listOfSum[index+1] # this shows the difference between the numbers that are next to each other
        bestSum = bestSum + bestDifference
        best.append(bestDifference)
    for index in range(len(best)):
        bestRelative.append(best[index] / bestSum)
    
    
    
    for relative in bestRelative:
        
        if math.sqrt(relative*relative) < 0.15:
            bestList.append(relative)
    
    lowestIndex = bestRelative.index(bestList[0])
    print("LOWEST INDEX IS ", lowestIndex)
    
    bestK = k[lowestIndex]
    print("FINAL BEST NUMBER OF CLUSTER IS", bestK)
    
    print("*****************FINISH CLUSTER HURRAY *****************", clusterList[lowestIndex])
    
    bestCluster = clusterList[lowestIndex]  
    return bestCluster, bestK

def visualize(datadict, bestCluster, bestK):
    colors = [[0,1,0],[1,0,0],[0,0,1],[1,0,1], [1,1,0], [0,1,1], [1,0.4,0], [0, 0.2, 0.4], [0.2, 0, 0.5], [0.1, 0.5, 0], [0, 0.5, 0.2], [0.4, 1, 0.1], [0.3, 0, 0.5], [0.1, 0, 0.8]]
    for number in bestCluster:
        for index in range(bestK):
        
            for akey in number[index]:
                datapoint = datadict[akey]
                plt.plot(datapoint[0], datapoint[1], 'o', color = (colors[index]))
        plt.show()
                
                    
def clusterAnalysisAirlines(dataFile):
   airDict = readAirlineFile(dataFile)
   (airClusters,whatever) = createClusters(airDict, 20)
   (airBest,whatever2) = findBestK(airClusters,whatever)
   airVisualize = visualize(airDict,airBest, whatever2)
    

clusterAnalysisAirlines("airplanes.txt")

                        
                        
                    
                


          
            
                
            
        
        


    
    
        

