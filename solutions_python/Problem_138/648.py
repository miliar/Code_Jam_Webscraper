import sys

def main():
    fi = open('input','r')
    testcases = int(fi.readline().rstrip('\n'))
    for t in range(testcases):

        tot = int(fi.readline())
        naimoi_list = map(float, fi.readline().split(' '))
        kevin_list = map(float, fi.readline().split(' '))

        kevin_list.sort()
        naimoi_list.sort()

        # deceitful war
        # K's largest to smallest
        i = tot - 1
        naiomi__count = tot - 1
        decietful_points = 0
        while i >= 0:
            if kevin_list[i] > naimoi_list[naiomi__count]:
                # take n's smallest
                #n_small_count += 1
                pass
            else:
                decietful_points += 1
                naiomi__count -= 1
            i -= 1

        #print "Deceitful war = ",n_points_dec

        # war
        # N's largest to smallest
        i = tot - 1
        k_small_count = 0
        k_large_count = tot - 1
        war_points = 0

        while i >= 0:
            if kevin_list[k_large_count] < naimoi_list[i]:
                # give smallest k
                #k_small_count += 1
                war_points += 1
            else:
                k_large_count -= 1

            i -= 1

        #print "War = ", n_points_war

        fh = open('output.txt','a')
        fh.write("Case #"+str(t+1)+": "+str(decietful_points)+" "+str(war_points))
        fh.write('\n')
        fh.close()
    return
main()