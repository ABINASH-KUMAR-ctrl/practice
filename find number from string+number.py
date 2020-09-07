import re
s=input("enter file name as m.txt ")
fh=open(s)
numbank=[]
alpabetANDnum=[]
for line in fh:
    word=line.split()
    for a in word:
        for b in a:
            if b.isnumeric()==True:
                try:
                    a=int(a)
                    numbank.append(a)
                    break
                except:
                    alpabetANDnum.append(a)
                    break
print(numbank,"len of num",len(numbank))
print(alpabetANDnum)
print(sum(numbank))
s=0
s=s+sum(numbank)
nmber=[]
for n in alpabetANDnum:
    nmber=nmber+(re.findall('[0-9]+',n))
    
print(nmber)
for m in nmber:
    s=s+int(m)
print(s)
    
                    
                    
                

