from math import floor
aaa = open("a.txt","r").readlines()
f=open("b.txt","w")
f.write("")
f.close()
supernumbers=[]
for i in range(0,len(aaa)):
    line = aaa[i]
    if len(line.strip().split(" "))>2:
        continue
    f = int(line.strip())
    numbers=aaa[i+f].replace("\n","").strip().split(" ")
    supernumbers.append(numbers)
for i in range(0,len(supernumbers),2):
    if i%2==1:
        continue
    set1=set(supernumbers[i])
    set2=set(supernumbers[i+1])
    set3=set1.intersection(set2)
    nn = floor(float(i)/2.0)+1
    print nn
    if not set3:
       f=open("b.txt","a")
       f.write("Case #%d: Volunteer cheated!\n" % nn)
       f.close()
    elif len(set3)>1:
       f=open("b.txt","a")
       f.write("Case #%d: Bad magician!\n" % nn)
       f.close()
    else:
       f=open("b.txt","a")
       f.write("Case #%d: %s\n" % (nn, list(set3)[0]))
       f.close()

    
