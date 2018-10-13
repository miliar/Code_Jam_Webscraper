f = open('a_large.in', 'r')
g = open('a_out.txt', 'w')

data = [line for line in f]
T = data.pop(0)

for case, d in enumerate(data):
    s_max, shystring = d.split()
    S = [int(i) for i in shystring]
    invites = 0
    standing = 0
    for k, num_people in enumerate(S):
        if standing >= k:
            standing += num_people
        else:
            invites = max(invites, (k-standing))
            standing += num_people
    print 'Case #%d: %d' %(case + 1, invites)
    g.write('Case #%d: %d\n' %(case + 1, invites))
f.close()
g.close()
