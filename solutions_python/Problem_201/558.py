import sys

numTests = int(sys.stdin.readline())
tests = []

# Read all tests
for i in range(numTests):
    t = sys.stdin.readline()
    tests.append(t)

# Solve them
for i in range(numTests):
    problem_string = tests[i].split(' ')
    problem = [int(x) for x in problem_string]

    stalls = problem[0]
    persons = problem[1]

    count = stalls-1
    inserted = 1
    next_step = 2

    if persons == 1:
        res_min = count // 2
        res_max = count - res_min
        print 'Case #' + str(i+1) + ': ' + str(res_max) + ' ' + str(res_min)
        continue


    while (inserted + next_step) < persons:
        count -= 2 * (next_step // 2)
        inserted += next_step
        next_step *= 2
        #print 'count: ' + str(count)
        #print 'next_step: ' + str(next_step)


    count -= 2 * (next_step // 2)
    #print 'previous count ' + str(count)
    if count < 0:
        count = 0
    #print 'count [final]: ' + str(count)
    #print 'next_step: ' + str(next_step)

    div = count // (next_step*2)
    rem = count % (next_step*2)

    res_min = div
    res_max = div

    #print 'div: ' + str(div)
    #print 'rem: ' + str(rem)
    #print 'inserted: ' + str(inserted)
    #print 'persons: ' + str(persons)
    #print 'next_step: ' + str(next_step)

    pos = persons - inserted - 1
    #print 'pos: ' + str(pos)
    if rem > pos:
        res_max += 1
    if rem > (next_step + pos):
        res_min += 1

    print 'Case #' + str(i+1) + ': ' + str(res_max) + ' ' + str(res_min)
