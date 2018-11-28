import sys
sys.stdout = open('c.out', 'w')
sys.stdin  = open("c.in", 'r')
sys.setrecursionlimit(1500)
T = int(raw_input())
import math

def solve():
    Hd, Ad, Hk, Ak, B, D = map(int, raw_input().split())
    if Ad < Hk and Ak - D >= Hd:
        return "IMPOSSIBLE"

    import math
    buff = map(lambda b: b + math.ceil(float(Hk) / (Ad + b*B)), range(100))
    b = 0, buff[0]
    for x in range(1, 100):
        if buff[x] < b[1]:
            b = x, buff[x]
    turns_to_kill = b[1]
    #print turns_to_kill
    simul_turns = 0
    simul_h = Hd
    simul_a = Ak
    turns_to_d = [None] * 101
    turns_to_d[0] = (0, Hd)
    for i in range(1, 101):
        dying = False
        while simul_h <= max(simul_a - D, 0):
            if dying:
                turns_to_d[i] = (float('inf'), float('inf'))
                break
            simul_h = Hd - simul_a
            simul_turns += 1
            dying = True
        if turns_to_d[i] == (float('inf'), float('inf')):
            break
        simul_turns += 1

        simul_a = max(simul_a - D, 0)
        simul_h -= (simul_a)
        turns_to_d[i] = (simul_turns, simul_h)


    best_turns = float('inf')
    #print turns_to_d
    for d, (turns, curr_h) in enumerate(turns_to_d):
        if turns == float('inf'):
            break
        else:
            buffs_attacks_remaining = turns_to_kill
            curr_ak = max(0, Ak - d*D)
            while buffs_attacks_remaining > 0:
                dying = False
                while curr_h <= curr_ak and buffs_attacks_remaining > 1:
                    if dying:
                        turns = float('inf')
                        break
                    dying = True
                    curr_h = Hd - curr_ak
                    turns += 1
                    #print "dying"
                    #print turns, curr_h, buffs_attacks_remaining
                buffs_attacks_remaining -= 1
                curr_h -= curr_ak
                turns += 1
                #print turns, curr_h, buffs_attacks_remaining
            #print d, turns
            best_turns = min(best_turns, turns)
    if best_turns == float('inf'):
        return "IMPOSSIBLE"
    return best_turns





for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)