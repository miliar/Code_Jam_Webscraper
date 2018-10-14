from __future__ import division, print_function

# fname_in =  'A-small-attempt0.in'
fname_in = 'A-large.in'
fname_out = fname_in.replace('.in', '.out')

fin = open(fname_in, 'r')
fout = open(fname_out, 'w')

Ncases = int(fin.readline().strip())

for jcase in range(0, Ncases):

    smax, schain = fin.readline().strip().split()

    smax = int(smax)

    s = [int(c) for c in schain]
    # print((jcase, s))
    people_clapping = s[0]

    invitations = 0

    for i in range(1, len(s)):

        if people_clapping < i:
            people_needed = i - people_clapping
            invitations += people_needed
            people_clapping += people_needed + s[i]
        else:
            people_clapping += s[i]

    outline = 'Case #%i: %i' % (jcase+1, invitations)
    print(outline)
    fout.write(outline + '\n')


fin.close()
fout.close()


