# Uian Sol Gorgonio <sol.uian@gmail.com>
# Apr 1 2015
# Problem A. Standing Ovation
#
# ad-hoc
#

nTests = int(raw_input())

for nt in xrange(1, nTests + 1):
    n, s_max = raw_input().split()

    sum_stand = 0
    invites = 0
    for i in xrange(len(s_max)):
        if sum_stand < i:
            invites += (i - sum_stand)
            sum_stand += (i - sum_stand)
        sum_stand += int(s_max[i])

    print 'Case #%d: %d' % (nt, invites)
