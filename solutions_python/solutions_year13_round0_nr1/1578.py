'''
Created on Apr 13, 2013

@author: jo
'''
def check(A):
    xi = {i:0 for i in range(4)}
    xj = {i:0 for i in range(4)}
    oi = {i:0 for i in range(4)}
    oj = {i:0 for i in range(4)}
    for i, row in enumerate(A):
        for j, e in enumerate(row):
            if e in ["X", "T"]:
                xi[i]+=1
                xj[j]+=1
            if e in ["O", "T"]:
                oi[i]+=1
                oj[j]+=1
    if any(x==4 for x in xi.values()) or any(x==4 for x in xj.values()) or all(x in ["X", "T"] for x in [A[i][i] for i in range(4)]) or all(x in ["X", "T"] for x in [A[i][3-i] for i in range(4)]):
        return "X won"
    elif any(x==4 for x in oi.values()) or any(x==4 for x in oj.values()) or all(x in ["O", "T"] for x in [A[i][i] for i in range(4)]) or all(x in ["O", "T"] for x in [A[i][3-i] for i in range(4)]):
        return "O won"
    elif sum(x for x in xi.values())+sum(o for o in oi.values())<16:
        return "Game has not completed"
    else:
        return "Draw"
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
    
def main():
    result = []
    lines = read_input("/Users/Jo/Downloads/A-small-attempt2.in")
    A = []
    for line in lines[1:]:
        if len(line)>1:
            A.append(line[:-1])
        else:
            if len(A)>0:
                result.append(check(A))
                A = []
    write_output(result, "/Users/Jo/Downloads/A-small-attempt2.out")
    
if __name__ == '__main__':
    main()