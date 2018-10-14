import time
starttime = time.time()

f = open("A-large.in", "r")
f2 = open("A-large.out", "w")

try:
    T = int(f.readline().strip())

    a = b = 0
    p = ''
    curPaths = {}
    curPath = curPaths
    newPaths = []
    count = 0
    
    for i in range(T):
        count = 0
        curPaths = {}
        curPath = curPaths
        newPaths = []
        [a, b] = map(int, f.readline().strip().split(' '))

        # read existing directories
        for j in range(a):
            p = f.readline().strip().split('/')

            for k in p:
                if not k:
                    continue
                if not curPath.has_key(k):
                    curPath[k] = {}

                # navigate path
                curPath = curPath[k]
                
            curPath = curPaths
            
        # read new directories
        for j in range(b):
            p = f.readline().strip().split('/')
            
            for k in p:
                if not k:
                    continue
                if not curPath.has_key(k):
                    curPath[k] = {}
                    count += 1

                # navigate path
                curPath = curPath[k]

            curPath = curPaths    

        s = "Case #%d: %d" % (i+1, count)
        f2.write(s + "\n")
        
    f2.flush()
    
finally:
    f.close()
    f2.close()

print (time.time() - starttime)
