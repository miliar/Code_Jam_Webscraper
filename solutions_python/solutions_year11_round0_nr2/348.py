fin, fout = open("input.txt", "r"), open("output.txt", "w")
c, d, n = 0, 0, 0
clist, dlist, nstr = [], [], ""

def read_info():
    global fin, fout, c, d, n, clist, dlist, nstr  
    c, d, n = 0, 0, 0
    clist, dlist, nstr = [], [], ""
    inp = fin.readline().split()
    pos = 0
    c = int(inp[pos])
    for i in range(c):
        pos += 1
        clist.append(inp[pos])
    pos += 1
    d = int(inp[pos])
    for i in range(d):
        pos += 1
        dlist.append(inp[pos])
    pos += 1
    n = int(inp[pos])
    nstr = inp[pos+1]
    return 0

stack = []

def normalize_stack():
    global stack
    for i in clist:
        j = len(stack)-2
        if len(stack) > 1 and ((i[0] == stack[-1] and i[1] == stack[j]) or (i[1] == stack[-1] and i[0] == stack[j])):
            del stack[-1]
            del stack[j]
            stack.append(i[2])
            normalize_stack()
            return 0
    for i in dlist:
        for j in range(len(stack)-1):
            if (stack[-1] == i[0] and stack[j] == i[1]) or (stack[-1] == i[1] and stack[j] == i[0]):
                stack = []
                return 0
    return 0

def make_result():
    global stack
    read_info()
    stack = []
    for i in nstr:
        stack.append(i)
        normalize_stack()
    return "["+", ".join(stack)+"]\n"

t = int(fin.readline())
for i in range(1, t+1):
    fout.write("Case #%d: "%i + make_result())
fin.close(); fout.close()