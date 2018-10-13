import sys

def main():
    with open(sys.argv[1]) as f:
        N = int(f.readline())
        #print N
        for i, line in enumerate(f):
            smax, audience = line.split()
            smax = int(smax)
            paid_applauders = start_applause(smax, audience)
            print "Case #%d: %d" % (i+1, paid_applauders)
    return

def start_applause(smax, audience):
    applauders = 0
    paid_applauders = 0
    for shyness_level, members in enumerate(audience):
        members = int(members)
        if applauders <= shyness_level:
            paid_applauders += shyness_level - applauders
            applauders = shyness_level
        applauders += members
    return paid_applauders

main()
