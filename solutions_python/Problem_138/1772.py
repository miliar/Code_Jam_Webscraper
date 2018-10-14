import sys

def compute(t):
    tot = int(sys.stdin.readline())
    n = map(float, sys.stdin.readline().split(' '))
    k = map(float, sys.stdin.readline().split(' '))

    k.sort()
    n.sort()

    # deceitful war
    # K's largest to smallest
    i = tot - 1
    n_small_count = 0
    n_large_count = tot - 1
    n_points_dec = 0
    while i >= 0:
        if k[i] > n[n_large_count]:
            # take n's smallest
            n_small_count += 1
        else:
            n_points_dec += 1
            n_large_count -= 1
        i -= 1

    #print "Deceitful war = ",n_points_dec

    # war
    # N's largest to smallest
    i = tot - 1
    k_small_count = 0
    k_large_count = tot - 1
    n_points_war = 0

    while i >= 0:
        if k[k_large_count] < n[i]:
            # give smallest k
            k_small_count += 1
            n_points_war += 1
        else:
            k_large_count -= 1

        i -= 1

    #print "War = ", n_points_war

    fh = open('output.txt','a')
    fh.write("Case #"+str(t)+": "+str(n_points_dec)+" "+str(n_points_war))
    fh.write('\n')
    fh.close()
    return

def main():
    for t in range(int(raw_input())):
        compute(t+1)

main()