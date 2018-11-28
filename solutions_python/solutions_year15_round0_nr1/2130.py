
def f(ovation_string):
    ovation_string_parts = ovation_string.split(" ")
     
    ovation = []
    for c in ovation_string_parts[1]:
        i = int(c)
        ovation.append(i)
    n = len(ovation)

    friends = 0
    num_up = 0
    for i in range(0, n):
        num_shy = ovation[i]
        if num_shy == 0:
            continue
        if num_up >= i:
            num_up += num_shy
            continue
        delta = i - num_up
        friends += delta
        num_up += delta + num_shy
    return friends

fi = open("input.txt", "r").readlines()
for i in range(1, len(fi)):
    fi[i] = fi[i].replace("\n", "")
    print "Case #" + str(i) + ": " + str(f(fi[i]))


