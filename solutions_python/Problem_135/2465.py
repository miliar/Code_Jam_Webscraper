def solve():
    row1 = input()
    data1 = [set([int(j) for j in raw_input().split()]) for i in range(4)]
    row2 = input()
    data2 = [set([int(j) for j in raw_input().split()]) for i in range(4)]
    solution = data1[row1-1] & data2[row2-1]
    if solution == set():
        return "Volunteer cheated!"
    if 1 == len(solution):
        return str(solution.pop())
    else:
        return "Bad magician!"

a = input()
for i in range(a):
    print "Case #{0}: {1}".format(i+1, solve())
