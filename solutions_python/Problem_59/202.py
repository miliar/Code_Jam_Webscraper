'''
Created on 2010-05-22

@author: lawford
'''

def add_r(tree, path):
    cnt = 0
    print("tree="+str(tree))
    print("path="+str(path))
    if len(path) == 0:
        return cnt
    if not tree.has_key(path[0]):
        tree[path[0]] = {}
        cnt = cnt +1
    cnt = cnt + add_r(tree[path[0]], path[1:])
    return cnt

def alg(din, dout):
    print("===")
    print(din)
    print(dout)
    
    tree = {}
    for entry in din:
        add_r(tree, entry.split('/')[1:])
        
    print(tree)
    
    cnt = 0
    for entry in dout:
        cnt = cnt + add_r(tree, entry.split('/')[1:])
        
    return [cnt]

if __name__ == '__main__':
    fname = "A"
#    f = open(fname+".in.txt", "r")
    f = open("/raid/downloads/firefox/A-large(3).in", "r")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

    piece1 = f.readline()
    while piece1 != '':
        [n,m] = map(int, piece1.split(" "))
        din = []
        dout = []
        for i in range(0, n):
            din.append(f.readline().rstrip())
        for i in range(0, m):
            dout.append(f.readline().rstrip())
            
        result = alg(din, dout)
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        piece1 = f.readline()
        cnt = cnt+1
    fout.close()
    f.close()
