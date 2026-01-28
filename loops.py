a=[1,2,3,4,5,6,7,8,9]
result=""
print(a)
for i in range(len(a)):
    if i==8:
      result+= str(a[i])
    else:
        result+= str(a[i])+","


print(result)
