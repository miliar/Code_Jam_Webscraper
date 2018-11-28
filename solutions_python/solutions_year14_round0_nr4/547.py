def delim(line):
    items = []
    item = ''
    for c in line:
        if c != ' ':
            item += c
        else:
            items.append(item)
            item = ''
    items.append(item[:-1])
    return items

def strListToFloat(items):

    for i in range(len(items)):
        items[i] = float(items[i])
    return items
    

def solve(N,n,k):

    j = 0
    wins2 = 0
    for i in range(N):
        while j<N:
            if n[i]<k[j]:
                j += 1
                break
            else:
                wins2 += 1
            j += 1
        
    wins1 = 0
    for i in range(N):
        if n[-1] > k[-1]:
            wins1 += 1
            n = n[:-1]
            k = k[:-1]
        else:
            n = n[1:]
            k = k[:-1]
    return str(wins1) + ' ' + str(wins2)
 


f = open("D-large.in",'r')
outf = open('war_L.txt','w')

lines = f.readlines()
T = int(lines[0]) #number of cases
caseIndex = 1;
for i in range(T):
    N = int(lines[caseIndex])
    naomi = strListToFloat(delim(lines[caseIndex+1]))
    ken = strListToFloat(delim(lines[caseIndex+2]))
    naomi.sort()
    ken.sort()
    
    caseIndex += 3
    outf.write("Case #" + str(i+1) + ": " + solve(N,naomi,ken) + "\n")
    

outf.close()
