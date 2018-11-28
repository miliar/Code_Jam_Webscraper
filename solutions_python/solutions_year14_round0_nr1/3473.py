# Read in file
f = open('A-small-attempt1.in', 'r')
f2 = open('output.txt', 'w+')
N = int(f.readline())

# Loop through cases
for i in range(N):
    k1 = int(f.readline())
    # Read in first input
    u1 = ""
    for j in range(4):
        tmp = f.readline()
        if (j+1 == k1): u1 = tmp.split()
    k2 = int(f.readline())
    # Read in second input
    u2 = ""
    for j in range(4):
        tmp = f.readline()
        if (j+1 == k2): u2 = tmp.split()
    # Check for intersection
    u3 = set(u1).intersection( set(u2) )
    if len(u3) == 0:
        f2.write('Case #' + str(i+1) + ': Volunteer cheated!\n')
    elif len(u3) == 1:
        f2.write('Case #' + str(i+1) + ': ' + str(next(iter(u3))) + '\n')
    else:
        f2.write('Case #' + str(i+1) + ': Bad magician!\n')
    
f.close()
f2.close()
