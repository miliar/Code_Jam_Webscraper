def ispalin(x):
    y = str(x)[::-1]
    if str(x)==y:
        return 1
    return 0
t = int(raw_input()) #line to be uncommented
#z = open('input.txt')#line to be commented
#h = z.readlines()# line to be commented
#t = int(h[0])#line to be commented
x = t
e = []
f = []
#z = open('input.txt')
i=1
while i<=t:
    y = raw_input() #line to uncommented 
    #y = h[i] # line to be commented 
    m = y.split(" ")
    e.append(int(m[0]))
    f.append(int(m[1]))
    i += 1
array = []

i = 1L
while i<=10000001:
    if ispalin(i):
        j = i*i
        if ispalin(j):
            array.append(j)
            #print j
    i += 1




k = len(array)
ans = []

g = 0
while x:
    a = e[g]
    b = f[g]
    
    if a>array[k-1]:
        print "0\n"
        continue
    if b>array[k-1]:
        b = array[k-1]
    
    for i in range(k):
        if array[i]>=a:
            count1 = i
            break
    for i in range(k):
        if array[i]<=b:
            count2=i
    ans.append(count2-count1+1)
    x -= 1
    g += 1
i = 0

while i<len(ans):
    print "Case #%d: %d"%(i+1,ans[i])
    i+=1
    
