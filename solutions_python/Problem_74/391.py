#! /usr/bin/python
'''
Blue and Orange
'''

T = int(raw_input())

for i in range(T):
    Line = raw_input().split()
    N = int(Line[0])
    time = 0
    slacktime = [0, 0] 
    pos = [1, 1]
    for j in range(N):
        R = 'BO'.index(Line[j * 2 + 1])
        P = int(Line[j * 2 + 2])
        lastMoved = None
        correction = True
        #Moving
        if (pos[R] != P):
            # Distance to travel
            dist = abs(P - pos[R])
            
            #Time taken until switch press is dist + 1
            d_time = max(1, dist - slacktime[R] + 1)
            
            time += d_time
            pos[R] = P 

            slacktime[(R + 1) % 2] += d_time
            lastMoved = R
                
            slacktime[(R) % 2] = 0
        #Pressing
        else:
            time += 1
            slacktime[(R + 1) % 2] += 1
            slacktime[(R) % 2] = 0

    print "Case #%d: %d" % (i + 1, time)

    
