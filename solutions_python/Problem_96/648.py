t = input()
for testcase in range(1, t+1):
    instring = map(int, raw_input().split())
    n = instring[0]
    s = instring[1]
    p = instring[2]
    array = instring[3:]
    array.sort(reverse = True)
    i = 0
    while i < len(array) and array[i] >= p + max(p-1, 0) * 2:
        i += 1
    j = i
    while j < len(array) and array[j] >= p + max(p-2, 0) * 2:
        j += 1
    print "Case #" + str(testcase) + ": " + str(i + min(j-i, s))


