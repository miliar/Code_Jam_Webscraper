i = open("B-large.in",'r')
o = open("B-large.out",'w')

l = list(i)
l = [line[:-1] for line in l]
output = ""
ans = 0.0
rate = 2

def cookies(c,f,x):
    c = float(c)
    f = float(f)
    x = float(x)
    rate = 2.0
    ans = 0.0
    while((x/(rate + f) + c/rate) < x/rate):
        ans += c/rate
        rate += f
    return ans + x/rate
for x in range(int(l[0])):
    case = l[x+1].split()
    output = output +  "Case #%d: %s\n"%(x+1,str(cookies(float(case[0]),
                                                         float(case[1]),
                                                         float(case[2]))))

o.write(output)

