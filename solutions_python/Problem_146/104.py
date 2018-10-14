import itertools

def is_valid(train):
    found = set()
    last = train[0]
    found.add(train[0])
    for t in train:
        if t != last:
            if t in found:
                return False
            found.add(t)
            
        last = t
    return True

def num_valid(sets):
    count = 0
    for p in itertools.permutations(sets):
        if is_valid("".join(p)):
            count += 1
    return count


if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        sets = raw_input().split()
        print "Case #%d: %d" % (i, num_valid(sets))
