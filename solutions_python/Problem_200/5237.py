def isSorted(l):
     return all(a <= b for a, b in zip(l[:-1], l[1:]))
def reverseDigits(n):
    temp = n
    a  = []
    while temp > 0:
        a.append(temp%10)
        temp = int(temp/10)
    return a
f = open("B-small-attempt1.in","r")
s = f.readlines()
a = []
for i in s:
    a.append(int(i.rstrip('\n')))
t = a[0]
wani = a[1:]
ax = 0
for n in wani:
    while True:
        a = reverseDigits(n)
        b = a[::-1]
        c = isSorted(b)
        if c:
            o = open("output.txt","a")
            o.write("Case #"+str(ax + 1)+": "+str(n)+"\n")
            o.close()
            break
        else:
            n -=1
    ax +=1
