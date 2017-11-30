import math

def Entropy(pos,neg):
	tot=pos+neg
	if pos==0.0 and neg==0.0:
		return 0.0
	elif pos==0.0:
		return -(neg/tot)*math.log((neg/tot),2)
	elif neg==0.0:
		return -(pos/tot)*math.log((pos/tot),2)
	else:
		return -(pos/tot)*math.log((pos/tot),2)-(neg/tot)*math.log((neg/tot),2)

def Gain(instances,attribute,AttrAndValues):
	pos=neg=0
	for i in instances:
		if i[-1]=='Yes':
			pos+=1
		else:
			neg+=1
	#len([item[-1] for item in instances if item[-1]=='Yes'])
	ES=Entropy(float(pos),float(neg))
	sum=0.0
	for AttrValue in AttrAndValues[attribute]:
		attrPos=attrNeg=0
		for i in instances:
			if i[attribute]==AttrValue:
				if i[-1]=="Yes":
					attrPos+=1
				else:
					attrNeg+=1	
		sum=sum+(((float(attrPos+attrNeg))/float(len(instances)))*Entropy(float(attrPos),float(attrNeg)))
	return ES-sum
	
def DecisionTree(instances,AttrAndValues,Attributes,path=''):
		max=0
		root=0
		for i in range(len(AttrAndValues)):
			x=Gain(instances,i,AttrAndValues)
			#print(Attributes[i],x) #prints attribute and corresponding gain
			if x>max:
				max=x
				root=i
				
		#print('\n')	
		#print(Attributes[root],max) #prints attribute with max gain
		
		if path=='':
			path=path+"["+Attributes[root]+"]"
		else:
			path=path+"--->["+Attributes[root]+"]"
		
		newAttributes=[]
		for i in Attributes:
			newAttributes.append(i)
		newAttributes.pop(root)
		
		newAttrAndValues=[]
		for i in AttrAndValues:
			newAttrAndValues.append(i)
		newAttrAndValues.pop(root)			
		
		oldpath=path
		for i in AttrAndValues[root]:
			#print('**********************',i,'**********************')
			path=path+"--->"+i
			newinstances=[]
			for j in instances:
				if j[root]==i:
					j.pop(root)
					newinstances.append(j)
					
			attrPos=attrNeg=0
			for j in newinstances:
				#print(j) #prints instances in new instances
				if j[-1]=="Yes":
					attrPos+=1
				else:
					attrNeg+=1
			#print(attrPos,attrNeg)	
			
			if attrPos==len(newinstances):
				#print("Yes")
				path=path+"--->(Yes)"
				print(path)
			elif attrNeg==len(newinstances):
				#print("No")
				path=path+"--->(No)"
				print(path)
			else:
				DecisionTree(newinstances,newAttrAndValues,newAttributes,path)				
				
			#print('\n')
			path=oldpath

Attributes1=['outlook','temperature','humidity','wind']
AttrAndValues1=[['Sunny','Overcast','Rain'], ['Hot','Mild','Cool'],['High','Normal'],['Weak','Strong']]
instances1=[]
instances1.append(['Sunny', 'Hot', 'High', 'Weak', 'No'])
instances1.append(['Sunny', 'Hot', 'High', 'Strong', 'No'])
instances1.append(['Overcast', 'Hot', 'High', 'Weak', 'Yes'])
instances1.append(['Rain', 'Mild', 'High', 'Weak', 'Yes'])
instances1.append(['Rain', 'Cool', 'Normal', 'Weak', 'Yes'])
instances1.append(['Rain', 'Cool', 'Normal', 'Strong', 'No'])
instances1.append(['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'])
instances1.append(['Sunny', 'Mild', 'High', 'Weak', 'No'])
instances1.append(['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'])
instances1.append(['Rain', 'Mild', 'Normal', 'Weak', 'Yes'])
instances1.append(['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'])
instances1.append(['Overcast', 'Mild', 'High', 'Strong', 'Yes'])
instances1.append(['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'])
instances1.append(['Rain', 'Mild', 'High', 'Strong', 'No'])

DecisionTree(instances1,AttrAndValues1,Attributes1,path='')