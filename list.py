n = input("enter the list range:")
l = [input("Enter the list elements:") for _ in range(n)]
print "The list is:",l

sum = 0
for i in range (0,n):
 sum = sum + l[i]
 
print "sum:",sum
