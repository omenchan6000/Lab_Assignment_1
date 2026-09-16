L1=[1,6,4,2,7,8,4,3,6,9,1,2,4,7,9]
L2=[]
for i in L1:
    if i not in L2:
        L2.append(i)
print(L2)