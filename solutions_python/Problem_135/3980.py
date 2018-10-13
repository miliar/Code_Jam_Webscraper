import sys

f = open('small.in', 'r')
w = open('small.out', 'w')
n = int(f.readline())
print(n)
for i in range (1, n+1, 1):
    array1 = []
    array2 = []
    row1 = int(f.readline())
    for j in range(row1-1):
        f.readline()
    array1 = [int(x) for x in f.readline().split()]
    for j in range(4-row1):
        f.readline()
    #print (array1)
    row2 = int(f.readline())
    for j in range(row2-1):
        f.readline()
    array2 = [int(x) for x in f.readline().split()]
    for j in range(4-row2):
        f.readline()
    #print (array2)

    count = 0;
    magic = 0;
    for r1 in array1:
        for r2 in array2:
            if r1 == r2:
                magic = r1;
                count = count + 1
    if count == 1:
        w.write("Case #" + str(i) +": " + str(magic) + "\n")
    elif count > 1:
        w.write("Case #" + str(i) +": Bad magician!\n")
    else:
        w.write("Case #" + str(i) +": Volunteer cheated!\n")
f.close()
w.close()

    
