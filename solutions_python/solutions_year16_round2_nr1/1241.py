def solve(string):
    numbers  = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
    test = {0: 'Z', 1: 'ON', 2: 'W', 3: 'HR', 4: 'U', 5: 'FI', 6: 'X', 7: 'SV', 8: 'G', 9: 'IN'}
    t1 = {0: 'Z', 2: 'W', 4: 'U', 6: 'X', 8:"G"}
    t2 = {1: "O", 3: "R", 5: "F", 7: "S"}


    s= {}
    str2 = list(string)

    for i in t1:
        c = string.count(t1[i])
        if c > 0:
            s[i]=c
            for y in range(c):
                for j in numbers[i]:
                    str2.pop(str2.index(j))

    string = "".join(str2)
    for i in t2:
        c = string.count(t2[i])
        if c > 0:
            s[i]=c
            for y in range(c):
                for j in numbers[i]:
                    str2.pop(str2.index(j))

    #print str2

    if len(set(list("NINE")) - set(str2)) == 0:
        s[9]=str2.count("I")

    return "".join([str(i)*s[i] for i in sorted(s)])


test = int(raw_input())
for test_num in range(test):
    value = raw_input()
    print "Case #%d: %s"%((test_num+1), solve(value))
