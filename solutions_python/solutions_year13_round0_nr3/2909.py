f = open('input.txt')

t = int(f.readline())

def nums(s,e):
    c=0
    for i in range(s,e+1):
        if str(i)==str(i)[::-1]:
            if i**0.5==int(i**0.5) and str(int(i**0.5))==str(int(i**0.5))[::-1]:
                c+=1
    return c

ret=''
for i in range(t):
    temp = f.readline().split(" ")
    ret += 'Case #'+str(i+1)+": "+str(nums(int(temp[0]),int(temp[1])))+"\n"

o = file('output.txt','w')
o.write(ret)
o.close()
