'''
Created on 2011-05-07

@author: Development
'''

import Tkinter
import tkFileDialog
def getInputFile():
    tkroot = Tkinter.Tk()
    tkroot.wm_state('withdrawn')
    out = tkFileDialog.askopenfile(parent=tkroot)
    tkroot.destroy()
    return out

import sys
#outstrm = sys.stdout

import os
outstrm = open(os.path.expanduser("~/Desktop/outB.txt"), 'w')

def parseLine(linestr):
    line = linestr.split()
    
    combodict = {}
    comboresult = {}
    
    def addCombo(cmb):
        if not cmb[0] in combodict:
            combodict[cmb[0]] = []
        if not cmb[1] in combodict:
            combodict[cmb[1]] = []
        combodict[cmb[0]].append(cmb[1])
        combodict[cmb[1]].append(cmb[0])
        comboresult[cmb[0] + cmb[1]] = cmb[2]
        comboresult[cmb[1] + cmb[0]] = cmb[2]
    
    oppdict = {}
    
    def addOppose(opp):
        if not opp[0] in oppdict:
            oppdict[opp[0]] = []
        if not opp[1] in oppdict:
            oppdict[opp[1]] = []
        oppdict[opp[0]].append(opp[1])
        oppdict[opp[1]].append(opp[0])
    
    num_combos = int(line[0])
    for j in line[1:1+num_combos]:
        addCombo(j)
    
    num_opposes = int(line[1 + num_combos])
    for j in line[2+num_combos:2+num_combos+num_opposes]:
        addOppose(j)
    
    num_elements = int(line[2+num_combos+num_opposes])
    elements = line[3+num_combos+num_opposes]
    
    result = []
    for j in elements[:num_elements]:
        if(j in combodict and result and result[-1] in combodict[j]):
            j = comboresult[j + result[-1]]
            result = result[:-1]
        if j in oppdict and any([x in oppdict[j] for x in result]):
            result = []
        else:
            result.append(j)
    return result

if __name__ == '__main__':
    file = getInputFile()
    if(file == None):
        exit(-1)
    cur = file.readline()
    num_cases = int(cur, 10)
    
    
    
    for i in range(1,num_cases + 1):
        outstrm.write("Case #" + str(i) + ": [" + \
                      ', '.join(parseLine(file.readline())) + "]\n")


        