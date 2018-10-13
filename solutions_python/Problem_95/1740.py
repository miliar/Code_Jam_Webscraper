
import sys

#print sys.argv[1]

f = open(sys.argv[1],'r').readlines()


fkey = f[0:3]
fvalue = f[3:]

dic = {}

indexy = 0
for i in fkey:
    indexx = 0
    for j in i:
        #print j
        dic[j]=fvalue[indexy][indexx]
        indexx +=1
    indexy += 1

dic['y'] = 'a'
dic['q'] = 'z'
dic['e'] = 'o'
dic['z'] = 'q'

aa =  dic.keys()
aa.sort()

bb = dic.values()
bb.sort()


f = open(sys.argv[2],'r')
T = f.readline()
output = ""
outputdic = []

for i in f.readlines():
    for j in i:
        output += dic[j]
    #print output
    outputdic.append(output)
    output = ""

#print outputdic
num=0
for i in outputdic:
    num +=1
    a = "".join(i)
    print "Case #"+ str(num) + ": " + a,
