nt = int(raw_input())

def answer(people):
    standing = 0
    need_to_add = 0
    for i, c in enumerate(people):
        c = int(c)
        if c == 0:
            continue
        adding_this_iteration = 0
        if i > standing:
            adding_this_iteration = i - standing
        need_to_add += adding_this_iteration
        standing += c + adding_this_iteration
    return need_to_add

for i in range(nt):
    print "Case #{}: ".format(i+1),

    people = raw_input().split()[1]
    print answer(people)
    
