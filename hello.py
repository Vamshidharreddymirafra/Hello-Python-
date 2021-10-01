'''def even(x):
  while(1):
    if(x%2==0):
       print("It is even",x)
       break
    else:
        print("It is odd",x)
even(2)


for x in range(2):
  x=x+1
print(x)

def even(x):
      for x in range(1):
         if(x%2==0):
            print("It is even",x)
         else:
             print("It is odd",x)
even(2)





#list
x=["vamshi","siva","venky"]
for i in x:
    print(x)
#x.append("sp")


#tuple
y=("apple","orange","mango")
print(y)

#dict
z={"apple":"2","mango":"3","orange":"4"}
print(z.values())





x='I am vamshidhar'
z=x.split()
print(z)


x="hello hello world"
z=x.count("hello")
print(z)
'''

'''
i=2
while(i<10):
  i=i+1
  print(i*2)
  '''

'''
a=10
b=2
print(a//b)

x=int(input("enter number"))
if x >0:
  print("is positive")
else:
  print("is negative")
'''
'''

n=int(input("enter number"))
rev=0
while(n>0):
  dig=n%10
  rev=rev*10+dig
  n=n//10
  print("reverse",rev)

'''
'''
a=[1,2,3]
for i in a:
  print(i)

'''

import re



x='what is it'
y=re.split('what',x)
s=re.findall('what',x)
print(s)
print(y)
z=re.search('what',x)
print(z)
if(z):
  print('match found')
  print(z.group(0))
  print(z.start())
  print(z.span())
else:
    print('not found')

replace='What'
sx=re.sub('what',replace,x)
print(sx)






def func(name="vamshi"):
 print("the name is ",name)
    
func("vivek")




#y='vamshi vivek venky'
match=re.search('(\d) (\d)','7036 356 222')
print("match group"+match.group(1))
print("match grup 2"+match.group(2))
print(match.start())
print(match.end())


'''
x=[1,2,3]
for i in x:
  if(i is 2):
      print(i)
      pass
  if(i is 2):
      print("outside pass",i)


x=[1,2,3]
for i in x:
  if(i is 2,3):
      print(i)
      continue
#  if(i is 2):
      print("outside pass",i)

'''

'''
a=list()


a.append(20)
for i in a:
   print(i)
  '''



x={"vam":"10","vivi":"11"}
for a in x.items():
  print(a)






