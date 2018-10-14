inp = open('B-small-attempt0.in','r')
o = open('tidynumbers.txt','w')

output = []

def caller(strn):
    ini = strn[0]
    tocall = ""
    for i in strn:
        if int(ini) > int(i):

            ini = str(i)
            tocall = str(int(strn) - 1)

            break
        else:
            ini = str(i)


    if tocall == "":
        output.append(strn)
    else:
        caller(tocall)

T = int(inp.readline().rstrip())

for x in range(T):
    N = int(inp.readline().rstrip())
    strni = str(N)
    caller(strni)

for x in range(T):
    o.write("Case #"+str(x+1)+": "+output[x]+"\n")

inp.close()
o.close()







