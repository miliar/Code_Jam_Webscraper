T = int(raw_input())
for X in range(1, T+1):
    alien = raw_input()
    base = len(set(alien)) #num of unique chars
    if base==1:
        base+=1
    # now mapping
    mapping = {}
    mapping_used = set()
    next_mapping = 0
    for i, digit in enumerate(alien):
        if i==0:
            mapping[digit] = 1
            mapping_used.add(1)
        elif digit not in mapping:
            mapping[digit] = next_mapping
            mapping_used.add(next_mapping)
            next_mapping=max(mapping_used)+1

    place = 1
    V = 0
    for digit in reversed(alien):
        V += mapping[digit]*place
        place *= base

    print 'Case #%d: %d' % (X, V)

#4*4*4*1 4*4*0 + 4*2 + 3
 #   3*3*1 + 3*0 + 2
