
#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()

quat = {1:{1: 1, 2: 2, 3: 3, 4: 4},
        2:{1: 2, 2:-1, 3: 4, 4:-3},
        3:{1: 3, 2:-4, 3:-1, 4: 2},
        4:{1: 4, 2: 3, 3:-2, 4:-1}}

qmap = {"i": 2, "j": 3, "k": 4}
qrev = {1: "1", 2: "i", 3: "j", 4: "k"}

DEBUG=False

def mult_quat(x,y):
    if x*y > 0:
        return quat[abs(x)][abs(y)]
    else:
        return -quat[abs(x)][abs(y)]

def calc_sub(substr):
    if len(substr) == 0: return "1"
    val = qmap[substr[0]]
    for i in xrange(1, len(substr)):
        val = mult_quat(val, qmap[substr[i]])
    if val < 0: return "-"+qrev[abs(val)]
    return qrev[val]


def dijkstra_quaternion(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        num_char, num_repeat = map(int, input_file.readline().strip().split())
        partial_spell = input_file.readline().strip()
        all_spell = partial_spell * (num_repeat % 256)
        if calc_sub(all_spell) != "-1":
            results[i+1] = "NO"
            continue
        if partial_spell.count("i") == 0 and partial_spell.count("j") == 0:
            results[i+1] = "NO"
            continue
        if partial_spell.count("i") == 0 and partial_spell.count("k") == 0:
            results[i+1] = "NO"
            continue
        if partial_spell.count("j") == 0 and partial_spell.count("k") == 0:
            results[i+1] = "NO"
            continue
        num_char * 4

        print("Passed test")
        possible_correct = False

        if DEBUG: print(all_spell)
        print(all_spell[:50])
        for isublen in xrange(1,min(len(all_spell)-1, num_char * 4)):
            if possible_correct: continue
            isub = all_spell[:isublen]
            rest_spell = all_spell[isublen:]
            if DEBUG: print(" -- isub = "+isub)
            if DEBUG: print(" -- -- icalc = "+calc_sub(isub))
            if calc_sub(isub) == "i" and calc_sub(rest_spell) == "i":
                for jsublen in xrange(1,len(rest_spell)):
                    if possible_correct: continue
                    jsub = rest_spell[:jsublen]
                    ksub = rest_spell[jsublen:]
                    if DEBUG: print(" -- jsub = "+jsub)
                    if DEBUG: print(" -- -- jcalc = "+calc_sub(jsub))
                    if DEBUG: print(" -- ksub = "+ksub)
                    if DEBUG: print(" -- -- kcalc = "+calc_sub(ksub))
                    if calc_sub(jsub) == "j" and calc_sub(ksub) == "k":
                        possible_correct = True

        results[i+1] = "YES" if possible_correct else "NO"
    input_file.close()




def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v)+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    dijkstra_quaternion(input_filename)
    write_output()

#
