L=[1,4,2,5,7,3,5,7,8,3,7,9,1,2,4,6,8,9]
smallest=L[0]
largest=L[0]
for i in L:
    if i < smallest:
        smallest=i
    if i > largest:
        largest=i
print("Smallest:", smallest)
print("Largest:", largest)