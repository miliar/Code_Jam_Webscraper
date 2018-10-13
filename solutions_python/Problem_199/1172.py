import sys


def find_flips(S,K):
    flips = 0
    for i in range(len(S)-K+1):
        if S[i] == '+':
            pass
        else:
            flips += 1
            for j in range(K):
                if S[i+j] == '-':
                    S[i+j] = '+'
                else:
                    S[i+j] = '-'
    if '-' in S:
        return 'IMPOSSIBLE'
    else:
        return flips

output = []

with open(sys.argv[1], 'rb') as input_file:
    inp = input_file.readlines()
for line_num in range(1, int(inp[0])+1):
    S=list(inp[line_num].split()[0])
    K=int(inp[line_num].split()[1])
    output.append(('Case #'+str(line_num)+': '+str(find_flips(S,K))))
    output.append("\r\n")
output.pop()
with open(sys.argv[2], 'wb') as out:
    out.writelines(output)
