tests = int(raw_input())
for _ in range(1, tests+1):
    S_max, audience = raw_input().split()
    extras = 0
    current_standing = 0
    for i in range(len(audience)):
        if audience[i] is '0' and current_standing <= i:
            extras += 1
            current_standing += 1
        current_standing += int(audience[i])
    print 'Case #' + str(_) + ': ' + str(extras)