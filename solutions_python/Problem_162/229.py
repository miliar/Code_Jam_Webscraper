def solve(n):
    seen = set()
    queue = [1]
    steps = 1
    while True:
        next_queue = []
        for x in queue:
            if x == n:
                return steps
            p1 = x+1
            p2 = int("".join(reversed(str(x))))
            if p1 not in seen:
                seen.add(p1)
                next_queue.append(p1)
            if p2 not in seen:
                seen.add(p2)
                next_queue.append(p2)
        queue = next_queue
        steps += 1


if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        n = int(raw_input())
        print "Case #%d: %d" % (i, solve(n))
        
