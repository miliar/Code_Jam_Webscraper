inp = """3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b"""


inp = open("A-large.in").read()

lines = inp.split('\n')

def CreateFolder(paths):
    index = 0
    for p in paths:        
        tokens = p.split('/')                
        for ti in range(len(tokens)-1):
            t = tokens[1:][ti]
            
            root = '/'.join(tokens[1:ti+1])
            #print root, "#", t
            if(t in UNIQUE):
                if root in UNIQUE[t]:
                    #root = t
                    continue # don't need create
                else:
                    UNIQUE[t].append(root)
                    index += 1
                    #print "Add ", t, root, p
            else:
                UNIQUE[t] = [root]
                index += 1
                #print "Add ", t, root, p
            #root = t
        
    return index
                
#parent may have the same name

UNIQUE = {} # [name] [parent]
T = int(lines[0])
index = 1
for i in range(T):
    UNIQUE.clear()
    #print lines[index]
    N, M = map(int, lines[index].split(' '))
    index += 1

    #print N, M
    exists = []    
    for j in range(N):
        exists.append(lines[index])
        index +=1
        
        
    BE = CreateFolder(exists)
    #print exists, BE
    nonexists = []
    for j in range(M):
        nonexists.append(lines[index])
        index +=1

    

    BEE = CreateFolder(nonexists)

    #print nonexists , BEE    

    print "Case #%s: %s"%(i+1,BEE)
    
    
