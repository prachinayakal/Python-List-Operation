# List Operations

# 1.Repetition
# Repetation involves repetation of the list
list = [12,14,16,18,20]
i = list*2 
print(i)

# 2.Concatenation
# It concatenates the list mentioned on either side of the operator
list1 = [5,10,15,20]
list2= [4,3,5,8]
list3 = list1+list2
print(list3)


# 3.Length
# It is used to get the length of the list
list = [5,10,15,20,4,8,45]
len(list)

# 4.Iteration
# The for loop is used to iterate over the list elements
list4 = [5,20,4,8,45]
for i in list4:
    print(i)


# 5.Membership
# It returns true if a particular item exists in a particular list otherwise false
list5 = [5,10,15,20]
print(8 in list5)
print(15 in list5)
print(163 in list5)
