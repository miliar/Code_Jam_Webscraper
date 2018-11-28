T = int(raw_input())

for tc in range(0, T):
        input = raw_input().split(' ')
       # print 'D,N', input
        D = int(input[0])
        N = int(input[1])

        H = {}
        for n in range(0, N):
                input = raw_input().split(' ')
                K = int(input[0])
                S = int(input[1])

                H[K] = S
#                print input


        H_key = H.keys()
        H_key.sort()
#        print H_key
        maxT = 0
        for k in H_key:
               # print k, H[k]
                dist1 = k + H[k] * maxT
                sped1 = H[k]

                
                #  First horse   
                if k == H_key[0]:
                        dist2 = dist1
                        sped2 = sped1
                elif sped1 < sped2:
                        #time to dest of prev horse
                        timeD = float(D - dist2) / sped2

                        #time to this horse of prev horse
                        timeH = float(dist1 - dist2) / (sped2 - sped1)

                        #print timeD,timeH
                        time = min (timeD,timeH)
                        maxT = maxT + time
                        dist2 = dist1 + sped1 * time
                        sped2 = sped1
                #print dist2,sped2,maxT

        if dist2 > D:
                dist2 = D
        maxT=maxT+float(D - dist2) / sped2  #time to dest
#        print maxT
        print 'Case #' + str(tc+1) + ': ' + '%.6lf' % (D/maxT) #+ ' - ' + str(maxT)
        
