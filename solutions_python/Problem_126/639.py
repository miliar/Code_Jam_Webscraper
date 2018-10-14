import sys

WAIT_TOTAL = 0
WAIT_CASE = 2

def process_input():

    cases_count = 0

    state = WAIT_TOTAL
    for line in sys.stdin.readlines():
        line = line.strip()
        line = ' '.join(line.split())
        if line != '':

            if state == WAIT_TOTAL:
                c = int(line)
                state = WAIT_CASE
            elif state == WAIT_CASE:
                cases_count += 1
                assert cases_count <= c
                (name, n) = line.split()
                n = long(n)
                ret = process_case2(name, n)
                sys.stdout.write('Case #' + str(cases_count) + ': ')
                print ret
            else:
                assert False

def process_case2(name, n):
    bag = []
    core_count = 0
    for i in range(0, len(name)):
        if not is_vowel(name[i]):
            #print 'not vowel', name[i]
            core_count += 1
        else:
            core_count = 0
        if core_count >= n:
            #print 'i-n+1+1',i-n+1+1
            for x in range(0, i - n + 1 + 1):
                for y in range(i, len(name)):
                    s = (x,y)
                    #print 's',s
                    if not s in bag:
                        bag.append(s)
    return len(bag)

def process_case(name, n):
    total = 0
    cores = 0
    core_count = 0
    last_core = None
    for i in range(0, len(name)):
        if not is_vowel(name[i]):
            #print 'not vowel', name[i]
            core_count += 1
        else:
            core_count = 0
        if core_count >= n:
            a = (i - n + 1) 
            b = (len(name) - i - 1)
            core = (i - core_count + 1, i)
            #if cores > 0 and substr(last_core, core):
            if cores > 0:
                subtotal = b + 1 - 1
            else:
                subtotal = (a + 1) * (b + 1)
            print 'a',a,'b',b, 'subtotal', subtotal,'i',i
            total += subtotal
            last_core = core
            cores += 1
    return total #+ cores

def substr(c1, c2):
    print 'core', c1, c2, c1[0] >= c2[0] and c1[1] <= c2[1]
    return c1[0] >= c2[0] and c1[1] <= c2[1]

def is_vowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


if __name__ == '__main__':
    process_input()


