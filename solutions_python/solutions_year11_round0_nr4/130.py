import sys

fin = open('D-large.in', 'r')
sys.stdout = open('D-large.out', 'w')

t = int(fin.readline())

for x in range(t):
    n = int(fin.readline())
    data = [int(y) for y in fin.readline().strip('\n').split(' ')]

    srted = list(data)
    srted.sort()

    # count number of wrong elements
    wrong = 0
    for y in range(n):
        if srted[y] != data[y]:
            wrong += 1

    print('Case #'+str(x+1)+': '+str(wrong))
    
sys.stdout.close()
fin.close()
