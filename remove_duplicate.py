marks=[]
n=int(input("Enter no of elements:"))
for i in range(n):
    value=int(input())
    marks.append(value)
print(marks)
sl=[]
for x in marks:
    if x not in sl:
        sl.append(x)
print(sl)        
