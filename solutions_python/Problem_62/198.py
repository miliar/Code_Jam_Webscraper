
infile = """2
3
1 10
5 5
7 7
2
1 1
2 2"""

infile = open("A-large.in").read()

ofile = open("output.txt","w")
lines = infile.split("\n")

Cache = {}

def func(a,b):
    total = 0
    for k in Cache:
        if k > a:
            if Cache[k][1] < b: total += 1
        else:
            if Cache[k][1] > b: total += 1

    Cache[a] = (a,b)
    return total

T = int(lines[0])
index = 1

for t in range(T):
    Cache.clear()
    N = int(lines[index])
    index += 1
    total = 0
    for n in range(N):
        a,b = map(int, lines[index].split(' '))
        index += 1

        #print a,b
        total += func(a,b)

    print total
    #index += 1
    ofile.write("Case #%s: %s\n"%(t +1, total))


ofile.close()
