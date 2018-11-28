#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2015 - Qualifiers - A Standing Ovation
#
# Author:      Ashish Nitin Patil
#
# Created:     11-04-2015
# Copyright:   (c) Ashish Nitin Patil 2015
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = input()

for test_case in range(1, T+1):
    smax, shyness = raw_input().split()
    smax = int(smax)
    friends_req = 0
    # 0 shyness audience is already clapping
    already_clapping = int(shyness[0])
    # highest shyness req adience will require special treatment
    for k in range(1, smax+1):
        k_count = int(shyness[k])
        if k >= already_clapping:
            friends_req += k - already_clapping
            already_clapping += k - already_clapping
        already_clapping += k_count
    print("Case #{0}: {1}".format(test_case, friends_req))
