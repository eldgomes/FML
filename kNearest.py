import math
import operator

classes=['Bad','Good']
classCount=[0,0]

k=3
instances=[]
instances.append([7,7,'Bad'])
instances.append([7,4,'Bad'])
instances.append([3,4,'Good'])
instances.append([1,4,'Good'])

new=[3,7,None]

for i in instances:
	distance=math.sqrt(math.pow((i[0]-new[0]),2)+math.pow((i[1]-new[1]),2))
	i.append(distance)
	
instances.sort(key=operator.itemgetter(-1))

for i in range(k):
	print(instances[i][2],instances[i][3])
	if instances[i][2]=='Bad':
		classCount[0]+=1
	else:
		classCount[1]+=1
		
if classCount[0]>classCount[1]:
	print(classes[0])
elif classCount[1]>classCount[0]:
	print(classes[1])
else:
	print("non-deterministic.more training examples needed")
	
	