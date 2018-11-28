attempt_list = ['C-test','C-small-1-attempt0','C-small-2-attempt0','C-large']
attempt = attempt_list[3]

import time
time.clock()

def solve(n,k):
    s_groups = {n:1}
    count = 0
    while k > 0:
        count += 1
        s_max = max(s_groups)
        s_max_count = s_groups.pop(s_max)
        k -= s_max_count

        sk = s_max-1
        s1 = sk//2
        s2 = sk-s1

        s_groups[s1] = s_groups.get(s1,0)+s_max_count
        s_groups[s2] = s_groups.get(s2,0)+s_max_count

    return str(max(s1,s2))+' '+str(min(s1,s2))

def main():
    fin = open(attempt + '.in', 'r')
    fout = open(attempt + '.out','w')

    numcases = int(fin.readline())

    for casenum in range(1,numcases+1):
        [n, k] = map(int, fin.readline().split())
        fout.write('Case #' + str(casenum) + ': ' + str(solve(n, k)) + '\n')

    fin.close()
    fout.close()

main()
print(time.clock())