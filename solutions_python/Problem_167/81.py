# Import the file
in_file = 'C-small-attempt0.in'
#in_file = 'C.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'C-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]

def IsPoss(D,V,C):
    for i in range(1,C+1):
        if V%i == 0 and V//i in D: return(True)
    if D == [] or V < min(D): return(False)
    for i,d in enumerate(D):
        for c in range(1,C+1):
            if IsPoss(D[(i+1):],V-d*c,C): return(True)
    return(False)
    pass

OUT = []
for k in range(Tt):
    # Enter code here
    C,D1,V = list(map(int,data[0].split(' ')))
    D = list(map(int,data[1].split(' ')))
    del data[:2]
    # Find the smallest number that cannot be expressed in the current denomination
    D = sorted(D,reverse=True)
    #print(D)
    Flag = True
    Count = 0
    while Flag:
        Flag = False
        for v in range(1,V+1):
            if not IsPoss(D,v,C):
                Flag = True
                D.append(v)
                Count += 1
                #print('Fail',v)
                break
    OUT.append(Count)
    pass

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
