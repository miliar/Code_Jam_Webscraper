

def do(thegraph):
    for a in thegraph:
        if (getDads(thegraph, a)):
            return("Yes")
            break;
    return "No"

def getDads(tgraph, node):
    dads = {}
    thelist = [node]
    while (len(thelist) > 0):
        curr = thelist.pop();
        for tmp in tgraph[curr]:
            if tmp in dads:
                return True
            else:
                dads[tmp] = True
                thelist.append(tmp)
    return False
    
    
def tograph(inline):
    contestantsTmp = inline.split(" ")
    contestants = []
    for i in range(1, len(contestantsTmp)):
        contestants.append(int(contestantsTmp[i]));
    return contestants

filename = "C:\\D\\codejam\\A-large.in"
out = open(filename + ".out", "w")
f = open(filename)
number = int(f.readline())
for i in range(number):
    graph = {}
    lines = int(f.readline())
    for a in range(1, int(lines) + 1):
        graph[a] = []
        line = f.readline().split(" ")
        for k in range(1, len(line)):
            graph[a].append(int(line[k]))    
    #print(graph)
    a = ("Case #" + str(i+1) + ": " + do(graph))
    print(a)
    out.write(a + "\n")
    
    