import os, sys, math

#__debug=True
__debug=False

def debug(str):
    if __debug:
        print "[DEBUG] %s" % str

def main():
    no_cases=int(sys.stdin.readline().strip())
    for i in range(1,no_cases+1):
        variables=sys.stdin.readline().strip().split(' ')
        s_max=int(variables[0])
        s_list=variables[1]
        guests_invited=0
        ovation=int(s_list[0])
        if s_max>0:
            debug(s_list)
            for j in range(1,s_max+1):
                if int(s_list[j])==0:
                    continue
                debug("ovation %d j %d" % (ovation, j))
                if j>ovation:
                    guests_invited+=(j-ovation)
                    ovation=j+int(s_list[j])
                else:
                    ovation+=int(s_list[j])
        print "Case #%d: %d" % (i, guests_invited)
    return 0


if __name__ == "__main__":
    main()
