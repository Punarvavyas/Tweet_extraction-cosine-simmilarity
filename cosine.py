
import math
import sys
import  re


term_list=[]

fileterms=open(sys.argv[1],'r+')
lines=fileterms.readlines()
for line in lines:
    term_list.append(line.strip())
print(term_list)

f1=open(sys.argv[2],'r+')
f2=open(sys.argv[3],'r+')

s1=f1.read()
s2=f2.read()
#print(s1.lower())
#print(s1)


s1=re.sub(r'([^A-Za-z0-9\_]+)',' ',s1)
s2=re.sub(r'([^A-Za-z0-9\_]+)',' ',s2)

#print(s1)
#print(s2)
v1=[]
v2=[]
for i in range(0,len(term_list)):
    x=s1.lower().split().count(term_list[i])
    v1.append(x)

for i in range(0,len(term_list)):
    x=s2.lower().split().count(term_list[i])
    v2.append(x)

#print(v1)
#print(v2)

sumationv1 = 0
sumationv1v2 = 0
sumationv2 = 0
for i in range(len(v1)):
    v1_coordinates = v1[i]
    v2_coordinates = v2[i]
    sumationv1v2 = sumationv1v2 + v1_coordinates * v2_coordinates
    sumationv1 = sumationv1 + v1_coordinates * v1_coordinates
    sumationv2 = sumationv2 + v2_coordinates * v2_coordinates

if sumationv2==0 or sumationv1==0:
    print("Cosine similarity not defined!")
else:

    cosine_value = sumationv1v2 / math.sqrt(sumationv1 * sumationv2)

    print("Cosine_similarity:", cosine_value)



