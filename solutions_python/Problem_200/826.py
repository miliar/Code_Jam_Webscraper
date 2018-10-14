__author__ = 'jlinenthal'

def isTidy(str):
    prevChar = 0
    for c in str:
        if c < prevChar:
            return False
        prevChar = c
    return True

#filename = "B-small-attempt0"
#filename = "BTest"
filename = "B-large"

infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

t = int(f_in.readline().strip())

for i in range(0,t):
    n = list(map(lambda x: int(x), list(f_in.readline().strip())));
    #print(str(n) + " " + str(isTidy(n)))

    n = n[::-1]
    index = 0
    while not isTidy(n[::-1]):
        if n[index] < n[index+1]:
            n[0:index+1] = [9]*(index+1)
            n[index + 1] = (n[index + 1] - 1) % 10
        #print(str(index) + " " + str(n))
        index += 1
    print("Case #{0}: {1}".format(i+1, str("".join(map(lambda x: str(x), filter(lambda x: x != 0, n[::-1]))))))
    f_out.write("Case #{0}: {1}\n".format(i+1, str("".join(map(lambda x: str(x), filter(lambda x: x != 0, n[::-1]))))))



#line = f_in.readline().strip()
#k = int(line.split()[0])
#c = int(line.split()[1])

