def wordprob(string):
    wordnum  = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
    t1 = {0: 'Z', 2: 'W', 4: 'U', 6: 'X', 8:"G"}
    t2 = {1: "O", 3: "R", 5: "F", 7: "S"}
    s= {}
    word1 = list(string)
    for i in t1:
        c = string.count(t1[i])
        if c > 0:
            s[i]=c
            for y in range(c):
                for j in wordnum[i]:
                    word1.pop(word1.index(j))

    string = "".join(word1)
    for i in t2:
        c = string.count(t2[i])
        if c > 0:
            s[i]=c
            for y in range(c):
                for j in wordnum[i]:
                    word1.pop(word1.index(j))



    if len(set(list("NINE")) - set(word1)) == 0:
        s[9]=word1.count("I")

    return "".join([str(i)*s[i] for i in sorted(s)])


test = int(raw_input())
for test_num in range(test):
    value = raw_input()
    print "Case #%d: %s"%((test_num+1), wordprob(value))