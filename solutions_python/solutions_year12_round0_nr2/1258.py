#!/usr/bin/python

import math

computed = {}

def main():
    with open('B-large.in', 'r') as f_in:
        inp = f_in.readline()

        case_cnt = int(inp)
        
        for caseIx in range(1, case_cnt + 1):
            computed.clear()
            
            inp = f_in.readline()
            scores = inp.split()

            goog_cnt = int(scores[0])
            surp_cnt = int(scores[1])
            best_val = int(scores[2])
            scores = scores[3:]

            cnt = 0
            for gIx in range(goog_cnt):
                
                score = int(scores[gIx])
                
                if score in computed.keys():
                    if computed[score] == '+':
                        cnt += 1
                    elif computed[score] == '=' and surp_cnt > 0:
                        cnt += 1
                        surp_cnt -= 1
                    elif computed[score] == '=' and surp_cnt == 0:
                        computed[score] = '-'
                    continue
                        
                x = math.floor((score - best_val) / 2.0)
                if x < 0:
                    computed[score] = '-'
                    continue
                
                if x > best_val - 2:
                    computed[score] = '+'
                    cnt += 1
                elif x == best_val - 2 and surp_cnt > 0:
                    computed[score] = '='
                    cnt += 1
                    surp_cnt -= 1
                else:
                    computed[score] = '-'

            with open('B-large.out', 'a') as f_out:
                f_out.write('Case #' + str(caseIx) + ': ' + str(cnt) + '\n')

main()
