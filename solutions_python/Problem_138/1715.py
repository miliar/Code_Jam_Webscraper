import sys

num_cases = int(sys.stdin.readline())
f = open('myfile3','w')

for z in range(0, num_cases):
    num_blocks = sys.stdin.readline()
    line1 = sys.stdin.readline()
    list1 = line1.split()

    line2 = sys.stdin.readline()
    list2 = line2.split()

    naomi = []
    ken = []
    for i in list1:
        naomi.append(float(i))

    for j in list2:
        ken.append(float(j))

    naomi.sort()
    ken.sort()
    ken2 = ken[:]

    wins = int(num_blocks)
    # play war
    for n in naomi:
        greater = filter(lambda x: x > n, ken2)
        if len(greater) > 0: 
            a = min(greater)
            ken2.remove(a)
            wins -= 1
        else:
            a = min(ken2)
            ken2.remove(a)

    # play deceiful war
    ken.sort(reverse=True)
    wins2 = int(num_blocks)
    for k in ken:
        greater = filter(lambda x: x > k, naomi)
        if len(greater) == 0:
            wins2 -=1
            a = min(naomi)
            naomi.remove(a)
        else:
            a = min(greater)
            naomi.remove(a)
        
    f.write("Case #" + str(z+1) + ": " + str(wins2) + " " + str(wins) + "\n")
                
