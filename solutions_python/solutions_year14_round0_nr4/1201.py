__author__ = 'st_lim'

ken = []
naomi = []

def perform_war(n, orig_naomi, orig_ken):
    war_result = 0
    deceit_result = 0
    count = 0
    naomi = list(orig_naomi)
    ken = list(orig_ken)
    # naomi largest > ken largest => ken will drop lowest
    for i in range(0,n):
        while len(naomi) > 0 and len(ken) > 0 and naomi[-1] > ken[-1]:
            naomi.pop()
            del ken[0]
            war_result += 1
            i += 1
        while len(naomi) > 0 and len(ken) > 0 and ken[-1] > naomi[-1]:
            naomi.pop()
            ken.pop()
            i += 1

    naomi = list(orig_naomi)
    ken = list(orig_ken)
    # naomi largest > ken largest => ken will drop lowest
    ken_id = 0
    for naomi_id  in range(n):
        if len(naomi) > 0 and len(ken) > 0 and naomi_greater_ken(naomi[naomi_id], ken[ken_id]):
            deceit_result += 1
            ken_id += 1

    result = "{0} {1}".format(deceit_result, war_result)
    return result

def naomi_greater_ken(naomi_val, ken_val):
    return (naomi_val - ken_val) > 0.00001

import sys
myfile = open(sys.argv[1], 'r')
myoutfile = open("{0}.out".format(sys.argv[1]), 'w')
n_cases = int(myfile.readline())
for i in range(1, n_cases + 1):
    n = int(myfile.readline())
    naomi = sorted(map(float, myfile.readline().split()))
    ken = sorted(map(float, myfile.readline().split()))

    result = perform_war(n, naomi, ken)
    output = "Case #{0}: {1}\n".format(i, result)
    print "Naomi: {0}".format(",".join(map(str, naomi )))
    print "Ken: {0}".format(",".join(map(str, ken )))
    print output
    myoutfile.write(output)