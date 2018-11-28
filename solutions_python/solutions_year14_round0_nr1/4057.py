mat = []
def get_raw(r):
    mat=[]
    for x in range(4):
        mat.append(set([int(x) for x in raw_input().split(" ")]))
    return mat[r-1]

t = input()
for I in range(t):
    r1 = input()
    s1 = get_raw(r1)
    r2 = input()
    s2 = get_raw(r2)
    esh = s1 & s2
    if(len(esh) == 1):
        print "case #"+str(I+1)+": "+str(list(esh)[0])
    elif(len(esh)>1):
        print "case #"+str(I+1)+": Bad magician!"
    else:
        print "case #"+str(I+1)+": Volunteer cheated!"
