import math

file = open('A-large.in', 'r')
target = open("ALarge.txt", 'w')

a = file.read().split("\n")

n = int(a[0])


for _i in range(n):
    levels = []
    num = int(a[2*_i+1])
    val = [int(x) for x in a[2*_i+2].split()]
    #print val
    val1 = 0
    top = 0
    for j in range(len(val)-1):
        if val[j] > val[j+1]: 
            val1 += (val[j] - val[j+1])
            top = max(top, val[j] - val[j+1])
    val2 = 0       
    for j in range(len(val)-1):
        val2 += min(top, val[j])
    
    #print val1, val2
    target.write("Case #"+str((_i)+1)+": "+ str(val1)+" "+ str(val2)+"\n")

target.close()
