def find_tidy(s):
    count = len(s)
    drop = -1
    for i in xrange(0, count - 1):
        if int(s[i + 1]) < int(s[i]):
            drop = i
    if drop == -1:
        return s
    while (drop > 0 and int(s[drop]) <= int(s[drop - 1])):
           drop -= 1
    if int(s[drop]) == 1:
           result = "9" * (count - 1)
    else:
           new_s = list(s)
           new_s[drop] = str(int(new_s[drop]) - 1)
           for i in xrange(drop + 1, count):
                new_s[i] = "9"
           result = "".join(new_s)
    return result


t = int(raw_input())
for i in xrange(1, t + 1):
    current_input = raw_input()
    print "Case #{}: {}".format(i,find_tidy(current_input))
