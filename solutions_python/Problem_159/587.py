def read_list_of(numtype):
    return map(numtype, raw_input().split())

def solve(l):
    # method 1

    method1 = 0
    for i, m in enumerate(l[1:]):
        if m < l[i]:
            method1 += l[i] - m

    method2 = 0
    max_speed = 0
    for i, m in enumerate(l[1:]):
        #print l[i], m
        if m < l[i]:
            speed = l[i]-m
            #print speed
            if speed > max_speed:
                max_speed = speed

    #print 'max speed', max_speed

    for i, m in enumerate(l[1:]):
        #print 'add',min(l[i], max_speed*10)
        method2 += min(l[i], max_speed)

    return method1, method2

def main():
    for case_number in xrange(int(raw_input())):

        raw_input()
        l = read_list_of(int)
        result = solve(l)

        print 'Case #%d: %d %d' % (case_number+1, result[0], result[1])

main()

#print solve([10,5,15,5])
#print solve([1,2,3,4])
#
# l = []
# import random
# for i in xrange(1000):
#     l.append(random.randint(0, 10000))
#
# print solve(l)
