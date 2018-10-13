def always(x,r,c):
    if x==1: #unit square
        return True
    if x==2: #dominoes
        return (r*c)%2==0
    if x==3: #L or I
        if (r*c)%3!=0: return False
        if r*c==3: return False #L in a 1x3
        else: return True
    else: # x==4
        if (r*c)%4!=0: return False
        if r>c: return always(x,c,r) #reducing cases to consider
        if r==1: return False #L
        if r==2: return False #2x2: L 2x4: Z
        if r==3: return True #box
        else: return True

def solve(x,r,c):
    if always(x,r,c): return "GABRIEL"
    else: return "RICHARD"

def parse(line):
    return [int(e) for e in line.split()]

if __name__=='__main__':
    cases=int(input())
    for i in range(cases):
        [x,r,c]=parse(input())
        print ("Case #"+str(i+1)+": "+solve(x,r,c))
