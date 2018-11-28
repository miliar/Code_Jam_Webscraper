i = open("A-small-attempt1.in",'r')
o = open("A-small-attempt1.out",'w')

l = list(i)
l = [line[:-1] for line in l]
output = ""
for x in range(int(l[0])):
    first = l[x * 10 + int(l[x * 10 + 1]) + 1].split()
    second = l[x * 10 + int(l[x * 10 + 6]) + 6].split()
    ans = [foo for foo in first if foo in second]
    if len(ans) == 0:
        y = "Volunteer cheated!"
    elif len(ans) == 1:
        y = ans[0]
    else:
        y = "Bad magician!"
    
    output = output +  "Case #%d: %s\n"%(x+1,y)

o.write(output)

