'''
Created on Apr 13, 2013

@author: jo
'''
def read_input(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    return lines

def write_output(results, path):
    f = open(path, "w")
    body = ""
    for i, result in enumerate(results):
        body+="Case #%d: %s\n" % (i+1, result)
    f.write(body)
    f.close()

def check(h, i, j, A):
    if all(h>=A[m][j] for m in range(len(A))) or all(h>=A[i][n] for n in range(len(A[i]))):
        return True
    return False

def mow(A):
    l = []
    for i, row in enumerate(A):
        for j, e in enumerate(row):
            l.append([e, i, j]) 
    l = sorted(l, key=lambda x: x[0])
    for x in l:
        if not check(x[0], x[1], x[2], A):
            return "NO"
    return "YES"
    
    
def main():
    lines = read_input("/Users/Jo/Downloads/B-large.in")
    result = []
    A = []
    m=0
    for i, line in enumerate(lines[1:]):
        e = line.split(" ")
        if i==m:
            if len(A)>0:
                result.append(mow(A))
                A = []
                
            m = i+int(e[0])+1
        else:
            A.append([int(x) for x in e])
        if i==len(lines[1:])-1:
            result.append(mow(A))
    write_output(result, "/Users/Jo/Downloads/B-large.out")
            
    
if __name__ == '__main__':
    main()