
""" I used these lines of code to generate the encryption string
s=['?']*26
f=open("C:/Users/hp/Desktop/codejam/input.txt")
testCase=int(f.readline())
a=[[]]*testCase
b=[[]]*testCase
for i in range(0,testCase):
    t=f.readline()
    t=t[:len(t)-1]
    a[i]=t.split(' ')
for i in range(0,testCase):
    t=f.readline()
    t=t[:len(t)-1]
    b[i]=t.split(' ')[2:]
for i in range(0,testCase):
    for j in range(0,len(a[i])):
        s1=a[i][j]
        s2=b[i][j]
        print s1,s2
        for k in range(0,len(s1)):
            s[ord(s1[k])-ord('a')]=s2[k]
s[25]='q'
s[16]='z'
t=""
for x in s:
    t+=x
print met
"""
f=open("C:/Users/hp/Desktop/codejam/input.txt","r")
writer=open("C:/Users/hp/Desktop/codejam/output.txt","w")
met="yhesocvxduiglbkrztnwjpfmaq"
testCase=int(f.readline())
a=[[]]*testCase
for i in range(0,testCase):
    writer.write("Case #")
    writer.write(str(i+1))
    writer.write(": ")
    t=f.readline()
    t=t[:len(t)-1]
    a[i]=t.split(' ')
    first=True
    for x in a[i]:
        y=''
        for c in x:
            y+=met[ord(c)-ord('a')]
        writer.write(y+" ")
    writer.write("\n")
