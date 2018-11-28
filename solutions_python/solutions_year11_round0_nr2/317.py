
def solve(C,O,L):
    elementList = []
    C = [(set(c[0:2]), c[2]) for c in C]

    for e in L:
        elementList.append(e)
        if updateComb(C, elementList):
            updateOppose(O, elementList)
        
    return '[%s]'%', '.join(elementList)

def updateComb(C, el):
    if len(el)<2:
        return False
    for c,t in C:
        if c == set(el[-2:]):
            el.pop()
            el.pop()
            el.append(t)
            return False
    return True
            
        
def updateOppose(O, el):
    if len(el)<2:
        return
    for o in O:
        if o[0] in el and o[1] in el:
            del el[:]
            return
            

input_file = 'B-large.in'
output_file = 'result.dat'
fin=open(input_file , 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    N = [x for x in fin.readline().split()]
    C = N[1:1+int(N[0])]
    i = int(N[0])+1
    O = N[i+1:(i+1+int(N[i]))]
    L = N[-1]
    ans = 'Case #%d: %s\n'%(t, solve(C,O,L))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()