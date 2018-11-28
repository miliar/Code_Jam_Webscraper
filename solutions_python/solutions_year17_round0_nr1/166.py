import sys

def solve(line):
    S = line[0]
    K = int(line[1])
    count = 0
    print S, K
    for i in range(0, len(S)):
        if S[i] == '+':
            continue
        else:
            if K <= len(S) - i and S[i] == '-':
                count += 1
                for j in range(i, i+K):
                    if S[j] == '-':
                        S = S[:j] + '+' + S[j+1:]
                    else:
                        S = S[:j] + '-' + S[j+1:]
            else:
                return -1
    return count
    

#in_file = open("input.txt", 'r')
#in_file = open("A-small-attempt0.in", 'r')
in_file = open("A-large.in", 'r')

out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split()

    sol = solve(line)

    if sol == -1:
        answer = "Case #" + str(case) + ": " + "IMPOSSIBLE" + "\n"
    else:
        answer = "Case #" + str(case) + ": " + str(sol) + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

