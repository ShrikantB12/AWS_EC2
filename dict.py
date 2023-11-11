li1 = [1,2,3,4,5]
li2 = [10,20,30,40,50]
di={}
for i,j in enumerate(li1):
  di.update({j:li2[i]})

print(di)
