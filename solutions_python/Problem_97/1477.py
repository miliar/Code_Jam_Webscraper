f = open('test_recycle')
g = open('out_recycle', 'w')
test_cases = int(f.readline())

def find_m(n):
    n = str(n)
    if len(n) == 1:
        yield int(n)
    else:
        for i in range(len(n)):
            yield int(n[-(i+1):] + n[:-(i+1)])

for case in range(0, test_cases):
    inp = f.readline().split()
    a = int(inp[0])
    b = int(inp[1])
    count = 0
    print ('-----')
    for i in range(a, b):
        for j in find_m(i):
            if i < j and j <= b:
                count += 1
    g.write("Case #{}: {}\n".format(case+1, count))
f.close()
g.close()
