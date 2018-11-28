import sys
import re

def needed_audience (input, smax):
    if smax==0:
        return (int(input[0]),0)
    (pre_audience,nb_inv) = needed_audience(input[:-1],smax-1)
    nb_smax = int(input[-1])
    if (nb_smax>0 and pre_audience<smax):
        add_inv = smax-pre_audience
        return (smax+nb_smax, nb_inv+add_inv)
    else:
        return (pre_audience+nb_smax, nb_inv)

file = sys.argv[1]

f = open(file)

nb_lines = int(f.readline())

for i in range(nb_lines):
    l = f.readline()
    (smax,input) = re.match('([0-9]) ([0-9]*)',l).groups()
    (total_audience,nb_invitees) = needed_audience(input, int(smax))
    print "case #%d: %d" % (i+1, nb_invitees)


