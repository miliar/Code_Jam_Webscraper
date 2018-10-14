#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    #nacteni 1 cisla
    text = sys.stdin.readline()[:-1]
    text.strip()
    
    list = []
    for i in range(len(text)):
        if text[i] not in list:
            list.append(text[i])
   
    if len(list) == 1:
        list.append('#')
    
    seque = [1,0] + range(2,40)
    
    dicti = {}
    for i in range(len(list)):
        dicti[list[i]] = seque[i]
    
    result = 0
    krat = 1
    for i in range(len(text)-1, -1, -1):
        result = result + dicti[text[i]] * krat
        krat = krat * len(list)
 
    print "Case #%d: %d" %(actual_case,result)
