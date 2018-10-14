f = open("D-small-attempt0.in",'r')
out = open("out.txt","w")

def func(x,r,c):
    if r*c % x != 0:
        return "RICHARD"
    elif x > r and x > c:
        return "RICHARD"
    elif x >= 5:
        return "RICHARD"
    elif x-1 >= min(r,c)*2:
        return "RICHARD"
    elif x==4 and ((r==2 and c==4) or (r==4 and c==2)):
        return "RICHARD"
    else:
        return "GABRIEL"

t = f.readline()
for it in range(int(t)):
    line = f.readline().strip('\n').split(' ')
    x = int(line[0])
    r = int(line[1])
    c = int(line[2])

    func(x,r,c)
    #L = f.readline().strip('\n').split(' ')
    #L = map(int,f.readline().strip('\n').split(' '))
    
    out.write("Case #"+str(it+1)+": " + str(func(x,r,c)) + "\n")
                
f.close()
out.close()
