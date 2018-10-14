#!/usr/bin/python

ifn = './sample.in'
ofn = './sample_ans.txt'

ifn = 'A-small-attempt1.in'
ofn = 'A-small-ans.txt'
#ifn = 'A-large-practice.in'
#ofn = 'A-large-ans.txt'
ofp = open(ofn, 'w')

def uniquechar(str):
        x = str[0]
        D = [1]
        for i in range(len(str)-1):
                if str[i+1] != str[i]:
                        x = x + str[i+1]
                        D.append(1)
                else:
                        D[-1] += 1
        return x,D

with open(ifn, 'r') as ifp:
        T = int(ifp.readline())
        for i in range(T):
                L = int(ifp.readline())
                C, is_win = [], 1
                char,D = uniquechar(ifp.readline().rstrip())
                C.append(D)
                for j in range(L-1):
                        x,D = uniquechar(ifp.readline().rstrip())
                        if x != char:
                                is_win = 0
                                break
                        C.append(D)
                        
                if is_win == 1:
                        tot_moves = 0
                        for j in range(len(D)):
                                moves = 0
                                a = [r[j] for r in C]
                                avg = sum(a)//L
                                for cnt in a:
                                        if cnt < avg:
                                                moves += avg - cnt
                                        else:
                                                moves += cnt - avg
                                tot_moves += moves
                        ofp.write("Case #%d: %d\n" % (i+1, tot_moves))                        
                else:
                        ofp.write("Case #%d: Fegla Won\n" % (i+1))

                
                
ifp.close()
ofp.close()
