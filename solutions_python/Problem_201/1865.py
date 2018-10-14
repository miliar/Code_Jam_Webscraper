#!/usr/bin/env python

def main(n, k):
    sol = [(0,n+1)]
    for i in range(1, n+1):
        l, r = sol[i-1]
        sol.append((l + 1, r - 1))
    sol += [(n+1,0)]

    return_l, return_r = 0, 0

    while k > 0:
        tmp = min(max(sol, key=lambda x: min(x[0], x[1])))
        pos = []
        for i in range(len(sol)):
            if min(sol[i][0], sol[i][1]) == tmp: pos.append(i)
        current_pos = pos[0]
        for i in pos:
            if max(sol[i][0], sol[i][1]) > max(sol[current_pos][0], sol[current_pos][1]):
                current_pos = i
        tmp_sol = sol
        tmp_sol[current_pos] = (0,0)

        for i in range(current_pos-1, -1,-1):
            if tmp_sol[i][0] == 0 and tmp_sol[i][1] == 0: continue
            tmp_sol[i] = tmp_sol[i][0], tmp_sol[i+1][1] +1

        for i in range(current_pos+1, len(tmp_sol)):
            if tmp_sol[i][0] == 0 and tmp_sol[i][1] == 0: continue
            tmp_sol[i] = tmp_sol[i-1][0] + 1, tmp_sol[i][1]

        sol = tmp_sol
        return_l = max(sol[current_pos-1][0], sol[current_pos+1][1])
        return_r = min(sol[current_pos-1][0], sol[current_pos+1][1])

        k -= 1

    return (return_l, return_r)




if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        l, r = main(n,k)
        print 'Case #{}: {} {}'.format(i, l ,r)

