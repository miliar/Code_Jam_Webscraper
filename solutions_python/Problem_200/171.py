import sys

def solve(line):
    num = str(line[0])
    if num < 10:
        return num
    
    size = len(num)
    for i in range(size - 1, 0, -1):
        if int(num[i]) >= int(num[i-1]):
            continue
        else:
            num = str(int(num[:i]) - 1)
            for j in range(0, size - i):
                num = num + "9"

    while num[0] == '0':
        num = num[1:]
    print num
    return int(num)

#in_file = open("input.txt", 'r')
#in_file = open("B-small-attempt0.in", 'r')
in_file = open("B-large.in", 'r')

out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split()

    sol = solve(line)

    answer = "Case #" + str(case) + ": " + str(sol) + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

