a=input()
b=[]
c=[]
d=int(len(a)/2)

for i in range(d): 
    b.append(eval(a[i]))
    
for j in range(d,len(a)):
    c.append(eval(a[j]))
    
if sum(b[:])==sum(c[:]):
    print('lucky')
else:
    print('fail')    


    