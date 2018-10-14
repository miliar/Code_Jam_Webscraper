'''
Created on Apr 12, 2013

@author: Phil
'''

def xofminbad(good,a):
    min = 1000
    x = 0
    for j in range(len(a)):
        r = a[j]
        for i in range(len(r)):
            if r[i]<min and good[j][i]==0:
                x = i
                min = r[i]
    return x

def yofminbad(good,a):
    min = 1000
    y = 0
    for j in range(len(a)):
        r = a[j]
        for i in range(len(r)):
            if r[i]<min and good[j][i]==0:
                y = j
                min = r[i]
    return y

def rowisless(a,y,m,good):
    r = a[y]
    for i in range(len(r)):
        if r[i]>m:
            return False
    return True

def colisless(a,x,m,good):
    for i in range(len(a)):
        r = a[i]
        if r[x]>m:
            return False
    return True

def allbadlocations(a,good,m):
    ls = []
    for j in range(len(a)):
        r = a[j]
        for i in range(len(r)):
            if r[i]==m and good[j][i]==0:
                ls.append([i,j])
    return ls

fname = input('In file: ')
namefile = fname.split('.')[0]

fr = open(fname, 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
output = ""
numCases = int(lines[0])
lnum = 1

for n in range(numCases):
    N = int(lines[lnum].split(' ')[0]) #num of rows
    M = int(lines[lnum].split(' ')[1]) #cols
    a = []
    for i in range(N):
        l = lines[lnum+i+1].split(' ')
        larr = [int(c) for c in l]
        a.append(larr)
    good = [[0 for x in range(M)] for y in range(N)]
    while sum(sum(x) for x in good)!=N*M:
        x = xofminbad(good,a)
        y = yofminbad(good,a)
        m = a[y][x]
        for coord in allbadlocations(a,good,m):
            x = coord[0]
            y = coord[1]
            if rowisless(a,y,m,good):
                #print('row '+str(y)+' is good')
                for j in range(len(good[y])):
                    good[y][j] = 1
                break
            elif colisless(a,x,m,good):
                #print('col '+str(x)+' is good')
                for i in range(len(good)):
                    good[i][x] = 1
                break
        else:
            #not possible!
            output += "Case #"+str(n+1)+": NO\n"
            break
    else:
        output += "Case #"+str(n+1)+": YES\n"
    lnum += N+1
        

output=output[:-1]
fw = open(namefile+'.out', 'w')
fw.write(output)
fw.close()