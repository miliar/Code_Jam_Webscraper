def intToList(x):
    return list(str(x))
def listToInt(x):
    return int("".join(x))
def sortInt(x):
    a = intToList(x)
    a.sort()
    return listToInt(a)
test_cases = int(raw_input())
for i in range(1, test_cases+1):
    N = int(raw_input())
    tidy = 1
    for q in range(1, N+1):
        if q > tidy:
            if sortInt(q) == q:
                tidy = q
    print "Case #" + str(i) + ": " + str(tidy)