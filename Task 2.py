'''l=[1,2,3,4,5,6,7,8,9,10]
a=l[0:5]


print("original list: ",l)
print("extracted first five elements: ",a)
print("Reversed extracted elements: ",a[::-1])
'''
l = [1,2,3,4,5,6,7,8,9,10]
a = l[0:5]

print("original list:", l)
print("extracted first five elements:", a)

# make a copy of a, then reverse it
b = a[0:6]      # copy of a
b.reverse()   # in-place reversal
print("Reversed extracted elements:", b)

