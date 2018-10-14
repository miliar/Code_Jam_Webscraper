fin = open("input.txt", "r")

tests_num = int(fin.readline())

for i in xrange(tests_num):
    [n, k] =[int(x) for x in fin.readline().split(" ")]
    #k_bin = [int(x) for x in "{0:#b}".format(k - 1)]
    mp = {n: 1}
    iter = 0
    while k > 0: # and iter < 20:
        iter += 1
        #print mp
        #print k
        new_mp = {}
        for it in sorted(mp.keys())[::-1]:
            k -= mp[it]
            if k > 0:
                if it % 2 == 0:
                    if not it/2 in new_mp.keys():
                        new_mp[it/2] = mp[it]
                    else:
                        new_mp[it/2] += mp[it]
                    if not it/2 - 1 in new_mp.keys():
                        new_mp[it/2 - 1] = mp[it]
                    else:
                        new_mp[it/2 - 1] += mp[it]
                else:
                    if not (it - 1)/2 in new_mp.keys():
                        new_mp[(it - 1)/2] = 2*mp[it]
                    else:
                        new_mp[(it - 1)/2] += 2*mp[it]
            else:
                mx = -1
                mn = -1
                if it % 2 == 0:
                    mx = it/2
                    mn = it/2 - 1
                else:
                    mx = (it-1)/2
                    mn = (it-1)/2
                print "Case #" + str(i + 1) + ": " + str(mx) + " " + str(mn)
                break

        mp = new_mp

fin.close()