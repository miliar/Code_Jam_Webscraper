def num_people_needed(audience):
    n = 0
    needed = 0
    for i,x in enumerate(audience):
        x = int(x)
        to_add = max(i-n, 0)
        needed += to_add
        n += x + to_add
    return needed
        

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        _, audience = raw_input().split()
        print "Case #%d: %d" % (i, num_people_needed(audience))
