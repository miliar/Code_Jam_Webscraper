testcases = input()

def run(testnum):
    asdf, audience = raw_input().split()
    current = 0
    friends = 0
    for i, v in enumerate(audience):
        if v != '0' and current < i:
            friends += i - current
            current += friends
        current += int(v)

    print "Case #" + str(testnum) + ": " + str(friends)
    return


for testcase in range(testcases):
    run(testcase + 1)
