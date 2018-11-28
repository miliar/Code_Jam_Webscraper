class Node:
    def __init__(self,name):
        self.name = name
        self.dic = {}
        self.ndic = {}

    def isExist(self,name):
        if name in self.dic:
            return True
        else: return False

    def add(self,name):
        self.dic[name] = True
        self.ndic[name] = Node(name)
        return self.ndic[name]
    def get(self,name):
        return self.ndic[name]

f_name = 'b'


fin = open(f_name + '.in',"r")
fout = open(f_name + '.out',"w")

c = 0;x = 0;n=0;m=0;
line = fin.readline()
x = int(line)
while x > 0:
    line = fin.readline()
    root = Node('/')
    v = root    
    n,m = [int(i) for i in line.split()]
    for i in xrange(0,n):
        t = fin.readline().split('/')
        v=root
        for j in xrange(1,len(t)-1):
            if v.isExist(t[j]) :v=v.get(t[j])
            else: v = v.add(t[j])
        if v.isExist(t[-1][:-1]) :v=v.get(t[-1][:-1])
        else:v.add(t[-1][:-1])

    s = 0              
    for i in xrange(0,m):
        t = fin.readline().split('/')
        v = root
        for j in xrange(1,len(t)-1):
            if v.isExist(t[j]) :v=v.get(t[j])
            else :
                s+=1
                v = v.add(t[j])
        if not v.isExist(t[len(t)-1][:-1]) :
            s+=1            
            v.add(t[len(t)-1][:-1])
    fout.write("Case #"+str(c+1) +": "+str(s) +"\n")
    c+=1
    x-=1


fin.close()
fout.close()
