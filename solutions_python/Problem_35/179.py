'''
Created on Sep 4, 2009

@author: indra
'''
import sys, os

filename = "B-large"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

WORD = "welcome to code jam"

N = int(reader.readline().rstrip())

H,W = 0,0
map,out = 0,0

def get_neighbors(y,x):
    ret = []
    if y>0:
        ret.append((y-1,x))
    if x>0:
        ret.append((y,x-1))
    if x+1<W:
        ret.append((y,x+1))
    if y+1<H:
        ret.append((y+1,x))    
    
    return ret

def flows(frm,to):
    fadjs = get_neighbors(frm[0],frm[1])
    alts = [map[fadj[0]][fadj[1]] for fadj in fadjs]
    mn = 0
    for alti in range(len(alts)):
        if alts[alti]<alts[mn]:
            mn = alti
    if alts[mn]>=map[frm[0]][frm[1]]:
        return False
    flows_to = fadjs[mn]
    ret = to[0]==flows_to[0] and to[1]==flows_to[1]
    return ret

def is_same_basin(cur, nbor):
    if out[nbor[0]][nbor[1]] != '0':
        return False
    return flows(cur,nbor) or flows(nbor,cur)

caseno = 1
while caseno<=N:
    case = reader.readline().rstrip()
    H,W = [int(x) for x in case.split(' ')]
    
    map = []
    out = []
    label = 'a'
    for h in range(H):
        line = reader.readline().rstrip()
        map.append([int(x) for x in line.split(' ')])
        out.append(['0' for x in range(W)])
    
    for yi in range(H):
        for xi in range(W):
            if out[yi][xi] != '0':
                continue
            q = [(yi,xi)]
            while len(q)>0:
                cy,cx = q.pop(0)
                out[cy][cx]=label
                neighbors = get_neighbors(cy,cx)
                for neighbor in neighbors:
                    if is_same_basin((cy,cx),neighbor):
                        q.append(neighbor)
            label = chr(ord(label)+1)
    
    writer.write("Case #%s:\n" % str(caseno))
    for outline in range(H):
        writer.write(' '.join(out[outline])+"\n")
    caseno+=1

writer.close()