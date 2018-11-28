import os
import sys
import re
import pdb

inf = open('input')
inp = inf.read().split('\n')
inf.close()

N = int(inp[0])
inp = inp[1:]
war_score_list = []
dec_score_list = []

for case_no in range(N):
    T = int(inp[0])
    inp = inp[1:]
    line1, line2 = inp[0:2]
    inp = inp[2:]
    naomi_war = map(lambda x:float(x),line1.split(' '))
    ken_war = map(lambda x:float(x),line2.split(' '))
    naomi_dec, ken_dec = naomi_war[:], ken_war[:]
    war_score, dec_score = 0, 0
    for block_no in range(T):
        if min(naomi_dec) > min(ken_dec):
            dec_score += 1
            naomi_dec.remove(min(naomi_dec))
            ken_dec.remove(min(ken_dec))
        else:
            naomi_dec.remove(min(naomi_dec))
            ken_dec.remove(max(ken_dec))
        if naomi_war[0] > max(ken_war):
            war_score += 1
            if block_no < T-1:
                naomi_war = naomi_war[1:]
                ken_war.remove(min(ken_war))
        else:
            ken_war.remove(min(filter(lambda x:x>naomi_war[0],ken_war)))
            if block_no < T-1:
                naomi_war = naomi_war[1:]
    war_score_list += [war_score]
    dec_score_list += [dec_score]

outf = open('output','w')
for case_no in range(N):
    outf.write('Case #%d: %d %d\n'%(case_no+1,dec_score_list[case_no],war_score_list[case_no]))
outf.close()
