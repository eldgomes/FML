Attributes=['outlook','temperature','humidity','wind']
instances=[]
instances.append(['sunny','hot','high','weak','no'])
instances.append(['sunny','hot','high','strong','no'])
instances.append(['overcast','hot','high','weak','yes'])
instances.append(['rain','mild','high','weak','yes'])
instances.append(['rain','cool','normal','weak','yes'])
instances.append(['rain','cool','normal','strong','no'])
instances.append(['overcast','cool','normal','strong','yes'])
instances.append(['sunny','mild','high','weak','no'])
instances.append(['sunny','cool','normal','weak','yes'])
instances.append(['rain','mild','normal','weak','yes'])
instances.append(['sunny','mild','normal','strong','yes'])
instances.append(['overcast','mild','high','strong','yes'])
instances.append(['overcast','hot','normal','weak','yes'])
instances.append(['rain','mild','high','strong','no'])

new=['sunny','cool','high','strong']

attrYes=[0,0,0,0]
attrNo=[0,0,0,0]

yes=0
no=0

for i in instances:
	if i[-1]=='yes':
		yes+=1
	else:
		no+=1

#print(yes,no)

for attr in range(len(Attributes)):
	#print(Attributes[attr])
	#print('\n')
	for i in instances:
		if i[attr]==new[attr]:
			#print(i[-1])
			if i[-1]=='no':
				attrNo[attr]+=1
			else:
				attrYes[attr]+=1

#attrYes=[2,3,3,3]
#attrNo=[3,1,4,2]
'''
for i in attrYes:
	print(i)

for i in attrNo:
	print(i)
'''
prod=1
for i in range(len(Attributes)):
	prod=prod*(attrYes[i]/float(yes))

probPos=prod*(float(yes)/float((yes+no)))

prod=1
for i in range(len(Attributes)):
	prod=prod*(attrNo[i]/float(no))
probNeg=prod*(float(no)/float((yes+no)))

probYes=probPos/float(probPos+probNeg)
probNo=probNeg/float(probPos+probNeg)


print('Yes:',probYes)
print('No:',probNo)

if probNeg>probPos:
	print("Decision:No")
elif probNeg<probPos:
	print("Decision:Yes")
else:
	print("Decision:equally likely")


