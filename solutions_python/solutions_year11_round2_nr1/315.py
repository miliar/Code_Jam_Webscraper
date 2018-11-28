#!/usr/bin/python


def cread(fd):
    return fd.readline().strip('\n')

def mean(x):
    t = 0.0
    n = 0
    for v in x:
        if v is not None:
            t += v
            n += 1
    if n==0:
        return None
    else:
        return t/n
            

def calc_wp(team):
    """
    Calculate the WP of a string
    """
    wp = 0.0
    NP = 0
    for c in team:
        if c=="1":
            wp += 1.0

        if c!=".":
            NP += 1
    if NP==0:
        return None
    else:
        return wp/NP

def calc_all_wp(match):
    return [ calc_wp(team) for team in match ]


def calc_owpj(team, j):
    # Maybe we just do not play against it
    if team[j]==".":
        return None

    # Remove the match of team j
    team = team[:j] + team[j+1:]
    return calc_wp(team)

def calc_all_owp(N, match):
    owp = [None]*N

    for i in xrange(N):
        # First calculate the OWPj of all the teams
        owpj = [ calc_owpj(match[k], i) for k in xrange(N) if k!=i ]
        for j in xrange(N-1):
            if j<i:
                k = j
            else:
                k = j+1
        # Now calculate the mean
        owp[i] = mean(owpj)
    return owp

def calc_all_oowp(N, match, owp):
    oowp = [None]*N
    for i in xrange(N):
        oth = [ owp[k] for k in xrange(N) if k!=i and match[i][k]!="." ]
        oowp[i] = mean(oth)
#        print("oowp[%d] = mean(%s) = " %(i, str(oth)) + str(oowp[i]))
    return oowp
                    

def solve(fd):
    """
    Read the matrix
    """

    # Number of teams
    N = int(cread(fd))

    # Now read N lines
    match = [None]*N
    for i in xrange(N):
        match[i] = cread(fd)

    # Now calculate the WP
    WP = calc_all_wp(match)
#    print("WP=" + str(WP))

    # Now the OWP
    OWP = calc_all_owp(N, match)
#    print("OWP=" + str(OWP))

    # And finally the OOWP
    OOWP = calc_all_oowp(N, match, OWP)
#    print("OOWP=" + str(OOWP))

    # With this apply the equation
    RPI = [None]*N
    for i in xrange(N):
        RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
        
    return RPI



import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(cread(fd))

for i in xrange(T):
    print("Case #%d:" % (i+1))
    RPI = solve(fd)
    for rpi in RPI:
        print("%.10f" % rpi)
    
fd.close()
    
               
    
