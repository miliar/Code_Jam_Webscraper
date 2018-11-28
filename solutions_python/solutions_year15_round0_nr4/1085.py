# Import the file
with open('D-small-attempt1.in','r') as f:
    data = f.readlines()

# Format the data
T = int(data[0])
del data[0]

Tesselate = []
Fail = []
for i in range(T):
    X,R,C = [int(el) for el in data[i].split(' ')]
    if X > 7:
        Tesselate.append(False) # Holes
        continue
    if X == 1:
        Tesselate.append(True) # Always possible
        continue
    # A necessary condition
    if R*C%X > 0:
        Tesselate.append(False)
        continue
    # Another necessary condition
    if X > max(R,C):
        Tesselate.append(False)
        continue
    if X == 2:
        # Only one 2-omino...
        Tesselate.append(True)
        continue
    if X == 3:
        if min(R,C) == 1:
            # Use a L shape
            Tesselate.append(False)
            continue
        if R%3 == 0 or C%3 == 0:
            Tesselate.append(True)
            continue
    if X == 4:
        if min(R,C) <= 2:
            # Use a 2 by 2 or a cross shape
            Tesselate.append(False)
            continue
        # 4 by 3 is possible, so is every other 4 by extension
        if R%4 == 0 or C%4 == 0:
            Tesselate.append(True)
            continue
    Fail.append([X,R,C])

print(T,len(Tesselate))

if T == len(Tesselate):
    with open('D.out','w') as f:
        for i in range(T):
            f.write('Case #{0}: {1}\n'.format(i+1,'GABRIEL' if Tesselate[i] else 'RICHARD'))
