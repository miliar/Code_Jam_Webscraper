import sys, os, re, collections, heapq, math

def print_result (case_num, result):
    print('Case #{}: {}'.format(case_num + 1, result))


def phase1 (activities):
    old = activities[-1][2]
    changes = 0
    buf = 0
    old_end = 0
    reserves = {'C':[], 'J':[]}
    self_time = {'C':0, 'J':0}
    for i,act in enumerate(activities):
        dur = act[1]-act[0]
        dur_between = act[0] - old_end
        if old == act[2]:
            reserves[act[2]].append(dur_between)
            self_time[act[2]] += dur_between
        else:
            changes += 1
            buf += dur_between
        self_time[act[2]] += dur
        old_end = act[1]
        old = act[2]

    last_fellow = activities[-1][2]
    first_fellow = activities[0][2]
    if first_fellow == last_fellow:
        reserves[first_fellow][0] += 60*24 - activities[-1][1]
        self_time[first_fellow] += 60*24 - activities[-1][1]
    else:
        buf += 60*24 - activities[-1][1]
    return changes, buf, reserves, self_time

def phase2 (L_self_time, H_self_time, H_reserves, changes):
    assert L_self_time < H_self_time
    H_reserves.sort(reverse=True)
    for dur in H_reserves:
        assert dur > 0
        assert L_self_time + H_self_time == 60*24, (L_self_time, H_self_time)
        L_self_time += dur
        H_self_time -= dur
        changes += 2
        if L_self_time >= H_self_time:
            return changes
    assert False

def solve (activities):
    activities.sort(key=lambda a:a[0])
    changes, buf, reserves, self_time = phase1 (activities)
    if abs(self_time['C'] - self_time['J']) <= buf:
        return changes
    if self_time['J'] < self_time['C']:
        L,H = 'J', 'C'
    else:
        L,H = 'C', 'J'
    return phase2(self_time[L] + buf, self_time[H], reserves[H], changes)

def main():
    for case_num in range(int(input())):
        ac, aj = map(int,input().split())
        activities = []
        for _ in range(ac):
            s,e = map(int,input().split())
            activities.append((s,e,'C'))
        for _ in range(aj):
            s,e = map(int,input().split())
            activities.append((s,e,'J'))
        print_result(case_num,solve(activities))

if __name__ == "__main__":
    main()
