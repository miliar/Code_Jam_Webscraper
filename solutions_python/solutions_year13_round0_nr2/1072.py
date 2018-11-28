'''
Created on 13.04.2013

@author: Verethragna
'''

def check():
    for j in range(h):
        for k in range(w):
            if rows[j][k] < mx[k] and rows[j][k] < my[j]:
                out.write("Case #" + str(i+1) + ": NO\n")     
                return
    out.write("Case #" + str(i+1) + ": YES\n")

path = input('Eingabedatei: ')
inp = open(path)
out = open(path+".out", "w")

n = int(inp.readline())

for i in range(n):
    reader = inp.readline().split(" ")
    h = int(reader[0])
    w = int(reader[1])
    if h == 1 or w == 1:
        for j in range(0,h):
            inp.readline()
        out.write("Case #" + str(i+1) + ": YES\n")
        continue
        
    rows = []
    for j in range(0,h):
        reader = inp.readline().split(" ")
        row = []
        for r in reader:
            row += [int(r)]
        rows += [row]
    
    my = []
    for row in rows:
        my += [max(row)]

    mx = []
    for j in range(w):
        c = 1
        for k in range(h):
            if rows[k][j] > c:
                c = rows[k][j]
        mx += [c]
                 
    check()
        
inp.close()
out.close()

print("DONE")
