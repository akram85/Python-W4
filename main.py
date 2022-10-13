# Sort a list
l=[10,12,3,5,8,4,9,1]
#l.sort();
x=[]

while(len(l)>0):
  min =l[0]
  for i in range(len(l)):
    if(l[i]<min):
        min =l[i];
  x.append(min)
  l.remove(min)
  
print(l)
print(x)