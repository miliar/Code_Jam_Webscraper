import math

def toBinary(k):
    return "{0:b}".format(k)

def solve(n,k):
    b = toBinary(k);
    for bit in b[1:]:
        #print(n)
        if (bit == '1'):
            n = math.floor((n-1)/2);
        else:
            n = math.ceil((n-1)/2);
    #print(n)
    #print(str(math.ceil((n-1)/2)) + " " + str(math.floor((n-1)/2)) + "\n")
    fout.write(str(max(math.ceil((n-1)/2),0)) + " " + str(max(math.floor((n-1)/2),0)) + "\n");
    #return max(math.ceil((n-1)/2),0), max(math.floor((n-1)/2),0);

def solve2(n,k):
    h = {n : 1}
    allValues = {}
    for i in range(k):
        maxVal = max(h);
        allValues[maxVal] = 1
        h[maxVal] -= 1
        if h[maxVal] == 0:
            del h[maxVal]
        val1 = math.ceil((maxVal-1)/2);
        val2 = math.floor((maxVal-1)/2);
        if not val1 in h:
            h[val1] = 0;
        if not val2 in h:
            h[val2] = 0;
        h[val1] += 1
        h[val2] += 1
        if i == k-1:
            #fout.write(str(val1) + " " + str(val2) + "\n")
            #print(str(val1) + " " + str(val2) + "\n")
            return val1, val2

def solve3(n,k):
    unvisited = {n : 1}
    visited = {}
    counter = 0;
    maxVal = max(unvisited);
    while (counter < k):
        maxVal = max(unvisited);
        visited[maxVal] = unvisited[maxVal];
        key1 = math.ceil((maxVal-1)/2);
        key2 = math.floor((maxVal-1)/2);
        if not key1 in unvisited:
            unvisited[key1] = 0;
        if not key2 in unvisited:
            unvisited[key2] = 0
        unvisited[key1] += visited[maxVal];
        unvisited[key2] += visited[maxVal];
        del unvisited[maxVal];
        counter += visited[maxVal];
    #return math.ceil((maxVal-1)/2), math.floor((maxVal-1)/2);
    fout.write(str(math.ceil((maxVal-1)/2)) + " " +str(math.floor((maxVal-1)/2)) + "\n");

lines = open("c:\codejam\C-small-2-attempt0.in").readlines()
fout = open("c:\codejam\C-small-2-attempt0.out", "w");
T = int(lines[0])
for tc in range(1, T+1):
    n = int(lines[tc].split()[0]);
    k = int(lines[tc].split()[1]);
    fout.write("Case #" + str(tc) + ": ");
    solve3(n,k);
fout.close()
