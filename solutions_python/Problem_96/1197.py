import csv
import itertools
f=open('C:/Users/chetan/Desktop/B-large.in','r')
n=f.readline()
b=f.readlines()
i=0
s=b
sum1=b
f.close()
while i<int(n):
    r = iter(csv.reader([b[i]], delimiter=' ', escapechar='\n'))
    b[i]=r.next()
    k=s[i]
    num=int(k[0])
    sup=int(k[1])
    prob=int(k[2])
    j=3
    res = 0
    totalSup = 0
    while j<len(s[i]):
        a= list(itertools.combinations_with_replacement(range(11), 3))
        l=0
        count=0
        valid=0
        while l<len(a):
            c=a[l]
            if (int(c[0])+int(c[1])+int(c[2]))==int(k[j]) and (int(c[2])-int(c[0])<=2) and (c[2]>=int(prob)):

                if (int(c[2])-int(c[0])==2):
                   count=count+1
                   
                valid=valid+1     
            l=l+1
       
        if(valid==1 and count==1):
            if(sup > 0):
                sup = sup - 1
                res = res +1
        elif(valid>0):
            res = res + 1
            totalSup = totalSup + count
        j=j+1

   
    s[i]='Case #%s: %s\n' % (i+1,res)
    i=i+1
f=open('C:/Users/chetan/Desktop/ou.txt','w')
f.writelines(s)
f.close()

