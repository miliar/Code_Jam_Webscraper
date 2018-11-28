
def annie(dest, lstHourses):
    slowest = 0
    for hourse in lstHourses:
        pos, max_speed = hourse
        remain = dest - pos
        time_need = float(remain) / max_speed
        if slowest < time_need:
            slowest = time_need
    return float(dest)/slowest

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        dest, n_horses = [int(s.strip()) for s in raw_input().split(" ")]
        hourses =[]
        for case in xrange(n_horses):
            pos, max_speed = [int(s.strip()) for s in raw_input().split(" ")]
            hourses.append((pos, max_speed))
        ans = annie(dest, hourses)
        print "Case #{}: {:.6f}".format(i, ans)
