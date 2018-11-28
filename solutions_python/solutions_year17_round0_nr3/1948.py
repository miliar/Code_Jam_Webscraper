import bisect
T = int(raw_input())

for tc in range(0, T):
        r = raw_input().split(' ')
        N = int(r[0])
        K = int(r[1])

        arr = [N]
        #print str(arr)
        for kc in range(0, K):
                mx = arr[-1]
                arr.pop(-1)

                Ls = (mx-1)/2
                Rs = (mx-0)/2

                bisect.insort(arr, Ls)
                bisect.insort(arr, Rs)

                #print str(arr)
                
        print 'Case #' + str(tc+1) + ': ' + str(Rs)+ ' '+str(Ls)
