if __name__ == "__main__":
    T = int(raw_input())
    for i in range(T):
        Smax, shies = [s for s in raw_input().split()]
        vals = []
        for s in shies:
            vals.append(int(s))
        friends = 0
        count = 0
        for k, val in enumerate(vals):
            if k > count:
                friends += (k-count)
                count += (k-count)
            count += val
        print "Case #%d: %d" %(i+1, friends)

