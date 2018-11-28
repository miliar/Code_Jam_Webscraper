import sys

rdLn = sys.stdin.readline

Tstr = rdLn()
Tstr = Tstr[:-1]
T = int(Tstr)

for i in range(1, T+1):
    r1 = int(rdLn()[:-1])
    set = []
    ans = []

    for j in range(1, 5):
        if (j == r1):
            nums = (rdLn()[:-1]).split(' ')
            for num in nums:
                set.append(num);
        else:
            rdLn()
            
    r2 = int(rdLn()[:-1])

    for j in range(1, 5):
        if (j == r2):
            nums = (rdLn()[:-1]).split(' ')
            for num in nums:
                if num in set:
                    ans.append(num)
        else:
            rdLn()

    output = "Case #{0}: ".format(i)

    if (len(ans) < 1):
        output += "Volunteer cheated!"
    elif (len(ans) > 1):
        output += "Bad magician!"
    else:
        output += ans[0]

    print output
