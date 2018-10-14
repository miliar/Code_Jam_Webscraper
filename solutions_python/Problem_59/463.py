#! /usr/bin/env python
import sys

# parsing input for a case

def read_line_int(f):
    line = f.readline()
    arr = line.split()
    t = [int(i) for i in arr]
    return t

   

     
# to have a nice name
def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]

def info(f):
    t2 = read_line_int(f)
    N = t2[0]#directories existing
    M = t2[1]#dir to create 
    return N,M


def path_in_tree(path,tree):
    return path in tree

def add_in_tree(path,tree):
    tree.append(path)

def create_in_tree(path,tree):
    cpt = 0
    for i in range(len(path)+1):
        if (path[:i] not in tree):
            cpt+=1
            print "j'ajoute le chemin"
            print path[:i]
            add_in_tree(path[:i],tree)
    return tree,cpt


def extract(line):
    p = []
    s=''
    for i in line:
        if (i == '/'):
            #print s
            p.append(s)
            s=""
        else: s+=i
    n = len(s)
    #remove \n
    if s[n-1] == '\n':
        s = s[:-1]
    p.append(s)
    return p[1:]

def read_line_path(f,tree):
    line = f.readline()
    path = extract(line)
    return create_in_tree(path,tree)
      
         
def caseprocess(f,i):
    tree = [[]]
    N,M = info(f)
    cpt = 0
    for j in range(N):
        #line = f.readline()
        #print extract(line)
        tree,c = read_line_path(f,tree)
    for j in range(M):
        tree , c = read_line_path(f,tree)
        cpt += c
    return "Case #%d: %d\n" % (i+1,cpt)


# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
    f = open(input,'r')
    t1 = read_line_int(f)
    T = t1[0]
    print "nb of cases :%d\n" % T
    o = open(output,'w')
    for i in range(T):
        print "case number %d processed\n" % i
        oline = caseprocess(f,i)
        print oline
        o.write(oline)
    o.close()
    f.close()
