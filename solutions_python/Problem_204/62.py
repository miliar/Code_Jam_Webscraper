import sys
import collections

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
        print "Case #%d: %d" % (i, solve())

def solve():

    def calc_cnt(base, package):
        l = 0
        r = (package / base + 1) * 2
        while  l < r :
            m = (l + r + 1) / 2
            if m * base * 90 > package * 100:
                r = m - 1
            else:
                l = m

        y = l

        l = 0
        r = (package / base + 1) * 2
        while  l < r :
            m = (l + r) / 2
            if m * base * 110 < package * 100:
                l = m + 1
            else:
                r = m

        x = l
        return (x, y)
    
    n, p = map(int, raw_input().split())
    base = map(int, raw_input().split())
    assert len(base) == n

    event_list = []

    pack_id = 0
    for i in xrange(n):
        packs = map(int, raw_input().split())
        assert len(packs) == p

        cur_dict = collections.defaultdict(int)
        for item in packs:
            calc_num = item
            cnt = calc_cnt(base[i], calc_num)
            if cnt[0] <= cnt[1]:
                pack_id += 1
                event_list.append((cnt[0], 1, i, cnt[1]))
                event_list.append((cnt[1] + 1, -1, i, cnt[1]))

    event_list.sort()
    pack_list = [[] for x in xrange(n)]

    last_event_time = None

    ans = 0
    
    for event in event_list:
        event_time = event[0]
        if event_time != last_event_time:
            ans += check(pack_list)

        if event[1] == 1:
            pack_list[event[2]].append(event[3])
        else:
            try:
                pack_list[event[2]].remove(event[3])
            except:
                pass

        last_event_time = event_time
        
    ans += check(pack_list)
    return ans

def check(pack_list):
    ans = 0
    while True:
        for p in pack_list:
            if len(p) == 0:
                return ans
        ans += 1
        for p in pack_list:
            p.remove(min(p))
main()
