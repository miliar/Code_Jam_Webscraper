attempt_list = ['A-test','A-small-attempt0','A-large']
attempt = attempt_list[1]

import time
time.clock()

def solve(s, k):
    s_len = len(s)

    # if all pancakes are already happy side up, skip further calcs
    if s == s_len*'+':
        return 0

    # convert to binary, where 1 is + and 0 is -
    s_goal = int('1'*s_len,2)
    s = s.replace('+','1')
    s = s.replace('-','0')
    s = int(s,2)

    # create dict for strings progress, string: shortest path
    s_all = {s:0}
    s_list_current = [s]
    s_list_next = []
    while s_list_current:
        # checking each new string
        for si in s_list_current:
            # flipping all possible ways
            for i in range(s_len-(k-1)):
                s_new = si^int('1'*k+'0'*i,2)
                if s_new not in s_all:
                    s_list_next.append(s_new)
                    s_all[s_new] = s_all[si]+1
        # reached the goal yet?
        if s_goal in s_all:
            return s_all[s_goal]
        # get ready for the next loop
        s_list_current = s_list_next[:]
        s_list_next = []

    return 'IMPOSSIBLE'


def main():
    fin = open(attempt + '.in', 'r')
    fout = open(attempt + '.out','w')

    numcases = int(fin.readline())

    for casenum in range(1,numcases+1):
        s, k = fin.readline().split()
        k = int(k)
        fout.write('Case #' + str(casenum) + ': ' + str(solve(s, k)) + '\n')

    fin.close()
    fout.close()

main()
print(time.clock())