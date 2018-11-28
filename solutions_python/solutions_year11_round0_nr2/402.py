#!/usr/bin/python
#coding:utf8


def magick(combos, opposed, elements):
    #print combos, opposed, elements
    #print elements
    combos_valid = [] 
    combos_result = []
    for i in combos:
        combos_valid.append(list(i[:2]))
        combos_valid.append(list(i[:2])[::-1])
        combos_result.append(i[2])
        combos_result.append(i[2])
    #print combos_result
    opposed_boom = []
    for i in opposed:
        opposed_boom.append(set(i))
    #print "opposed boom!", opposed_boom

    saida = []
    evaluando = []
    for i in range(len(elements)):
        evaluando.append(elements[i])
        if len(evaluando) > 2:
            evaluando.pop(0)
        #check combos
        #print elements[i:i+2]
        if evaluando in combos_valid:
            #print evaluando
            saida[-1] = combos_result[ combos_valid.index(evaluando)  ]
            evaluando = []
        else:
            saida.append(elements[i])
            for opps in opposed_boom:
                #print opps, opps.intersection(saida)
                if len(opps.intersection(saida)) == 2:
                    #print "boom!", opps, evaluando, saida
                    evaluando = []
                    saida = []
                    break
    return saida



"""
import re
def magick(combos, opposed, elements):
    #print combos, opposed, elements
    print elements
    for combo in combos:
        print  "replacing",combo[:2], combo[2], elements
        elements = re.sub("%s|%s"%(combo[:2],combo[:2][::-1]), combo[2], elements)
        print "final", elements 

"""

if __name__ == '__main__':
    num = input()

    for i in range(num):
        foo = raw_input()
        testcase = foo.split(" ")
        num_combos = int(testcase[0])
        #print num_combos
        combos = testcase[1:num_combos+1]
        #print "combos",combos
        num_opp = int(testcase[num_combos+1])
        #print num_opp
        opps = testcase[num_combos+2:num_combos+2+num_opp]
        #print "opposed", opps
        elements = list(testcase[-1])
        
        saida = ", ".join(magick(combos, opps, elements))

        print "Case #%s: [%s]"% (i+1, saida)
