n = int(input("Enter the number of elements: "))
L = []
for i in range(n):
    L.append(input())
reversed_L = []
for i in range(len(L)-1, -1, -1):
    reversed_L.append(L[i])
print("Original List:", L)
print("Reversed List:", reversed_L)