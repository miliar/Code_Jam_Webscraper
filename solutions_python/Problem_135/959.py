def a(A,B, arr1, arr2):
    nums_matching = []
    for first in arr1[A-1]:
        for second in  arr2[B-1]:
            if first == second:
                nums_matching.append(first)

    if len(nums_matching) == 1:
        return nums_matching[0]
    elif len(nums_matching) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


FILENAME = "A-small-attempt0"
f = open(FILENAME + '.in', 'r')
T = int(f.readline())
output = []

for i in range(T):
    A = int(f.readline())
    arrangement1 = []
    for j in range(4):
        temp = map(int,f.readline().split(' '))
        arrangement1.append(temp)
    B = int(f.readline())
    arrangement2 = []
    for j in range(4):
        temp = map(int,f.readline().split(' '))
        arrangement2.append(temp)
    
    output.append("Case #"+str(i+1)+": " + str(a(A, B, arrangement1, arrangement2)))
    print output[i]


f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()


