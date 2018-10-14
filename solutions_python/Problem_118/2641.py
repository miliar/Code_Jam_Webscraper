fairs = lambda it: [i + 1 for i in it if str(i + 1) == "".join(reversed(str(i + 1)))]
fair = fairs(xrange(10000))
square = [f**2 for f in fair]
fairandsquare = [s for s in square if str(s) == "".join(reversed(str(s)))]

count = lambda a, b: sum(1 for i in fairandsquare if a <= i <= b)

def process(f):
    i = iter(open(f))
    n = int(next(i).strip())
    
    with open("output", "w") as output:
        for j in range(n):
    	    a, b = map(int, next(i).strip().split())
            output.write("Case #{}: {}\n".format(j + 1, count(a, b)))

process("in2")