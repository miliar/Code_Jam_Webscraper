
def check_nondecreasing(num):
    for idx,dig in enumerate(num[:-1]):
        if dig > num[idx+1]:
            return False
    return True


N = int(raw_input())
for _ in xrange(N):
    test_case = int(raw_input().strip())
    for num in range(test_case+1)[::-1]:
        if check_nondecreasing(str(num)):
            print 'Case #%d: %d' % (_+1,num)
            break

