def findall(c, p):
    finds = []
    i = 0
    while p.count(c[0], i):
        i = p.find(c[0], i)
        finds.append(i)
        i+=1
    return finds
        

def count(welcome, phrase):
    if len(welcome)==0:
        return 1
    else:
        index = phrase.find(welcome[0]) 
        if index==-1:
            return 0
        else:
            finds = findall(welcome[0], phrase)
            n = 0
            for f in finds:
                n += count(welcome[1:], phrase[f:])
            return n

if __name__ == "__main__":
    welcome = 'welcome to code jam'
    file = open('in.txt','r')
    out =  open('out.txt','w')
    N = int(file.readline())
    case = 1
    for phrase in [l[0:-1] for l in file.readlines()]:
        out.write( "Case #%i: %.4i\n"%(case, count(welcome, phrase)))
        case+=1
    file.close()
    
    
    
        
