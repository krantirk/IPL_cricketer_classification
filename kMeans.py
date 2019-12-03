import numpy
import pandas
import math
import sys
import csv
import matplotlib.pyplot as plt

def euclidian_distance(x,y,a,b):
	sq_dist=((x-a)**2)+((y-b)**2)
	sq_dist=math.sqrt(sq_dist)
	return sq_dist

k=2
max_iterations=100
tolerance=0.01

df_run=pandas.read_csv(r"./runs.csv")
df_wicket=pandas.read_csv(r"./wickets.csv")
data_run=df_run.loc[:,'Runs':]
data_wicket=df_wicket.loc[:,'Wicket':]

data_run=numpy.array(data_run)
data_wicket=numpy.array(data_wicket)

centroidX=numpy.zeros(69)
centroidY=numpy.zeros(69)


centroidX=data_run
centroidY=data_wicket   

centroidX=centroidX[:3]
centroidY=centroidY[:3]

# print(centroidX)
# print(centroidY)


for i in range(max_iterations):

	classes=[]
	for j in range(k):
		temp=[]
		classes.append(temp)



	for j in range(len(data_run)):

		clusterId=0
		euc=euclidian_distance(centroidX[clusterId],centroidY[clusterId],data_run[j],data_wicket[j])

		for cluster in range(len(classes)):

			eucTemp=euclidian_distance(centroidX[cluster],centroidY[cluster],data_run[j],data_wicket[j])

			if eucTemp < euc:
					clusterId=cluster

				
			if eucTemp < euc:
					euc=eucTemp
				
			# print(cluster)	
		classes[clusterId].append((data_run[j],data_wicket[j]))


	newCentroidX=numpy.copy(centroidX)
	newCentroidY=numpy.copy(centroidY)
	# print(len(classes[0]))
	# print(len(classes[1]))
	# print(len(classes[2]))
	
	
	for classification in range(len(classes)):
		if len(classes[classification])>1:
			newCentroidX[classification]=numpy.average(classes[classification][0])
		if len(classes[classification])>1:
			newCentroidY[classification]=numpy.average(classes[classification][1])

	isOptimal=[]
	for k in range(3):
		isOptimal.append(False)

	for points in range(len(centroidX)):
		test=euclidian_distance(centroidX[points],centroidY[points],newCentroidX[points],newCentroidY[points])
		# print(test)
		if(test<tolerance):
			isOptimal[points]=True
			break


	if(isOptimal[0]==True and isOptimal[1]==True and isOptimal[2]==True):
		break


	centroidX=numpy.copy(newCentroidX)
	centroidY=numpy.copy(newCentroidY)	

print(centroidX)
print(centroidY)



# for i in range(len(classes)):

# 	print("CLASS ")
# 	print(i)
# 	classes[i]=numpy.array(classes[i])
# 	for j in range(len(classes[i])):

# 		print(classes[i][j])



colors=10*['r','b','g','c','k']
for point in range(len(centroidX)):
	plt.scatter(centroidX[point],centroidY[point],s=200,marker="x")

for classType in range(len(classes)):
	color=colors[classType]
	for point in range(len(classes[classType])):
		plt.scatter(classes[classType][point][0],classes[classType][point][1], color=color,s=10)


plt.show()











