# Sort a list
'''l=[10,12,3,5,8,4,9,1]
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
print(x)'''

'''#Matrix addition
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
m3=[[0,0,0],[0,0,0],[0,0,0]]

#m3 =m1+m2

for i in range(3):
  for j in range(3):
    m3[i][j] =  m1[i][j] +  m2[i][j]
print(m3)'''

'''Matrix multiplication'''
'''m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
# m3[i][j] = m1[i][k]*m2[k][j]
for i in range(3):
  for j in range(3):
    for k in range(3):
      m3[i][j] = m3[i][j]+ m2[i][k]*m1[k][j]
print(m3)'''
# Split 
line = '1 2 3 4'
output =line.split(' ')
numbers =[]

for i in output :
  numbers.append(int(i))
print (numbers)

x=2
print (x in numbers)

#GA1
x = 2 ** 5
x1 = x // 2
x2 = x1 // 2
x3 = x2 // 2
x4 = x3 // 2
x5 = x4 // 2
print(x1 + x2 + x3 + x4 + x5)

'''word = 'someone'
print(word[0])
print(word[-7])'''

'''sentence = input()
space = ' '
num_words = sentence.count(space) + 1
print(num_words)
'''
