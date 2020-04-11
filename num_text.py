import re
x=open('regex_sum.txt','r')
l=[]
for i in x:
    x=i.rstrip()
    l=l+re.findall('[0-9]+',i)
sum=0
for i in l:
    sum=sum+int(i)
print(sum)
