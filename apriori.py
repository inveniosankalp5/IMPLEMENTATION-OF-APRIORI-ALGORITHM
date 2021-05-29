fhand = open('<<FILENAME>>.txt')
data = []
for line in fhand:
	line = line.strip()
	li = line.split()
	li[1]=li[1].split(',')
	li[1].sort()
	data.append(tuple(li[1]))
#print(data)
minsup = int(input("Enter Minimum Support: "))
if minsup>len(data):
	quit()
L = []
C = []
dl = [] # duplicate L's 
L.append({})

#1st iteration of size 1
for itemset in data:
	for item in itemset:
		L[0][item] = L[0].get(item,0) + 1
dl.append( sorted(L[0].items()))
#print(dl)
#print(L[0], type(L[0])) 
#print(L[0].items())
for i in dl[0]:
	if L[0][i[0]] <  minsup:
		L[0].pop(i[0])
		#print(L[0][i])
dl[0] = sorted(L[0].items())
#print(L[0])
#print(dl[0])
C.append(L[0])
i=0
while len(L[i])>0:
	i+=1
	C.append({})
	for x1 in range(len(dl[i-1])):                      #Creating Candidate Key
		x = dl[i-1][x1]
		for y1 in range(x1+1,len(dl[i-1])):
			y = dl[i-1][y1]
			#print(x[0])
			#print(y[0])
			#print(x[0][:len(x[0])-1])
			if x[0][:len(x[0])-1]==y[0][:len(y[0])-1]:
				key = x[0][:len(x[0])-1] + x[0][-1]+y[0][-1]
				C[i][key] = 0
	#print(C[i])

	for k in C[i]:										#Counting occurences
		for itemset in data:
			f1 = 1
			for j in k:
				if j not in itemset:
					f1=0
					break
			if f1==1:
				C[i][k]+=1
	dl.append( sorted(C[i].items()))
	#print(C[i])
	#print(dl[i])

	for j in dl[i]:										
		if C[i][j[0]] < minsup:
			C[i].pop(j[0])
	L.append(C[i])
	dl[i] = sorted(L[i].items())
print(L)


