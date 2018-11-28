import math

inp = open('B-large.in', 'r')
out = open('B-large.out', 'w')

def single():
    return inp.readline().strip()

def mult():
    return inp.readline().strip().split()

def multint():
    x = inp.readline().strip().split()
    for a in range(len(x)):
        x[a] = int(x[a])
    return x

cases = int(inp.readline().strip())

for r in range(cases):

    x = multint()
    a = x[0]
    b = x[1]
    k = x[2]

    """
    result = 0
    for c in range(a):
        for d in range(b):
            if c & d < k:
                result += 1
    """

    if (k >= a or k >= b):
        result = a*b
    else:    

        result = k*b + k*a - k ** 2

        for c in range(k, a):
            for d in range(k, b):
                if c &d <k:
                    result+=1
    

    print("Case #" + str(r+1) + ": " + str(result))
    out.write("Case #" + str(r+1) + ": " + str(result) + "\n")    

inp.flush()
out.flush()
inp.close()
out.close()
