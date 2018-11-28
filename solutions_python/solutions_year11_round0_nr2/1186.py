#!/usr/bin/python

import sys
import math

answers = []

def print_answers():
    with open('output', 'w') as f:
        case_number = 0
        for answer in answers:
            #answer = answer.replace(" ", "").strip()
            answer = "[%s]" % ", ".join(answer)
            case_number += 1
            print "Case #%d: %s" %(case_number, answer)
            f.write("Case #%d: %s\n" % (case_number, answer))

def main(filename):
    with open(filename, 'r') as f:
        num_cases = int(f.readline().rstrip("\n"))
        print "Num Cases: %d"%num_cases
        for i in range(0, num_cases):
            print "Case: %s" % i
            line = f.readline().rstrip("\n")
            index_end = line.find(" ")
            num_combinations = int(line[0:index_end])
            combinations = []
            comb_end = index_end
            if num_combinations > 0:
                comb_end = index_end+4*num_combinations
                comb_str = line[index_end+1:comb_end]
                combinations = comb_str.split(" ")
            print "Num combinations: %s "%num_combinations
            print "Combinations: %s "%combinations
            num_opposed_index = comb_end + 1
            index_end = line.find(" ", num_opposed_index, num_opposed_index + 4)
            num_opposed = int(line[num_opposed_index:index_end])
            opposed_end = index_end + 1
            opposed=[]
            if num_opposed > 0:
                opposed_start = opposed_end
                opposed_end = num_opposed * 3 + opposed_start - 1
                opposed = line[opposed_start:opposed_end].split(" ")
            print "Num opposed: %s "%num_opposed
            print "Opposed: %s "%opposed
            opposed_index_end = line.find(" ", opposed_end+1)
            test_length = int(line[opposed_end:opposed_index_end])
            test_message = line[opposed_index_end + 1:]
            print "Test length: %s " % test_length
            print "Test message: %s " % test_message
            result = ""
            for a in test_message:
                result += a
                print "Result: %s " % result
                if len(result) > 1:
                    trial = result[-2:]
                    for c in combinations:
                        comb1 = c[0] + c[1]
                        comb2 = c[1] + c[0]
                        if trial == comb1 or trial == comb2:
#                            print "C0: %s, c1: %s, trial: %s" % (c[0], c[1], trial)
                            result = result[:-2]+c[2]
                            #print " Combine result: %s " % result
                    for o in opposed:
                        ind1 = result.find(o[0])
                        ind2 = result.find(o[1])
                        if ind1 != -1 and ind2 != -1:
                            max_index = max(ind1,ind2)
                            result = result[max_index+1:]
                           # print " Clear result: %s " % result
           # print "  End iteration result: %s "% result
            #answer = answer.rjust(3,'0')
            #print " Answer: %s"%answer
            answers.append(result)
            i+=1
        
    print_answers()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ./numbers.py 'inputfile.name'"
    else: 
        main(sys.argv[1])

