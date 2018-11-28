__author__ = 'Ruben'

def get_to_target(cur, tar):

    steps = 0

    while cur <= tar:
        cur += (cur-1)
        steps += 1

    return steps, cur

#file = open("round1a_a.txt")
file = open("A-small-attempt0.in")

cases = int(file.readline().strip())

for c in xrange(cases):
    c += 1

    tmp = file.readline().strip().split()
    a = int(tmp[0])
    n = int(tmp[1])
    n_motes = [int(x) for x in file.readline().strip().split()]
    n_motes.sort()

    #print "start:", a; print "start:", n_motes
    mote_cur = a; steps = 0

    if mote_cur == 1:
        steps = len(n_motes)
    else:

        while len(n_motes) > 0:
            #print n_motes

            if mote_cur > n_motes[0]:
                mote_cur += n_motes[0]
                n_motes = n_motes[1:]
            else:
                larger_count = len(n_motes)

                tmp_steps, temp_cur = get_to_target(mote_cur, n_motes[0]) #returns number of motes to add

                if tmp_steps < larger_count:
                    mote_cur = temp_cur
                    steps += tmp_steps

                    #mote_cur += n_motes[0]
                    #n_motes = n_motes[1:]
                else:
                    steps += larger_count
                    n_motes = []

    #print "end:", mote_cur
    #print "end:", n_motes

    print "Case #" + str(c)+": " + str(steps)


