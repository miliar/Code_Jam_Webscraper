import fileinput
import sys
#elements = {'Q','W','E','R','A','S','D','F'}

ele_list = []

def parse(seq):
    combines = {}
    cancels = {}
    tokens = seq.split()

    # Get Combines
    total_combines = int(tokens[0])
    i = 1
    for x in range(total_combines):
        word = tokens[i]
        i = i + 1
        letter1 = word[0]
        letter2 = word[1] 
        result = word[2]
        for tup in genTuples(letter1, letter2):
            combines[tup] = result        

    # Get cancels
    total_cancels = int(tokens[i])
    i = i + 1
    for x in range(total_cancels):
        word = tokens[i]
        i = i + 1
        letter1 = word[0]
        letter2 = word[1]    
        for tup in genTuples(letter1, letter2):
            l1 = tup[0]
            l2 = tup[1]
            if l1 in cancels:
                items = cancels[l1]
                items.append(l2)
                cancels[l1] =  items
            else:
                cancels[l1] = [l2]

    return tokens[-1],combines,cancels
    
def genTuples(letter1, letter2):
    return (letter1,letter2),(letter2,letter1)

def updateCancelSet(cancel_set, cancels, item, val=1):
    if item in cancels:
        booms = cancels[item]
        for boom in booms:
            if boom in cancel_set:
                count = cancel_set[boom]
                count = count + val
                cancel_set[boom] = count
            else:
                cancel_set[boom] = 1



def play(seq):
    msg,combines, cancels = parse(seq)

    cancel_set = {}#set([])
    ele_list = []
    #print combines, cancels
    for item in msg:
     #   print cancel_set, ele_list
        if len(ele_list) == 0:
            ele_list.append(item)
            updateCancelSet(cancel_set, cancels, item)
            continue
        last_letter = ele_list[-1]
        if (last_letter, item) in combines:
            updateCancelSet(cancel_set, cancels, last_letter, -1)
            #if last_letter in cancel_set:
             #   count = cancel_set[last_letter]
             #   count = count - 1
             #   cancel_set[last_letter] = count
            ele_list[-1] = combines[(last_letter, item)]
        elif item in cancel_set and cancel_set[item] > 0:
            ele_list = []
            cancel_set.clear() 
        else:#Copypaste
            ele_list.append(item)
            updateCancelSet(cancel_set, cancels, item)
                #cancel_set.update(cancels[item])


    return ele_list
       


cases = []
for i,line in enumerate(fileinput.input()):
    if i == 0:
        total_cases = int(line[0])
        continue
    cases.append(line.strip())

#Lord how does one easily print in the format they want?
for j,case in enumerate(cases):
    ele_list = play(case)
    #print ele_list
    print "Case #"+str(j+1)+':',
    if len(ele_list) == 0:
        print '[]'
    elif len(ele_list) == 1:
        print '[' + ele_list[0] + ']'
    else:
        for i,ele in enumerate(ele_list):
            if i == 0:
                print '[' + ele_list[i] + ',',
            elif i + 1 == len(ele_list):
                print ele_list[i] + ']'
            else:
                print ele_list[i] + ',',


#print parse("3 QRI SAM TUY 0   ")
#print parse("2 QRI SAM 3 TU YZ UZ   ")
#play("2 QRI SAM 3 TU YZ UZ 4 ABBA")
#print play("0 0 4 TERR")
#play("1 QRI 0 4 RRQR")
#print play("1 QFT 1 QF 7 FAQFDFQ")
#play("1 EEZ 1 QE 7 QEEEERA")
#play("0 1 QW 2 QW")
#print play("0 2 AS AD 3 DAS")
#print play("0 1 DR 8 REWARDED")
#print play("1 QFT 1 RF 2 QF")
#print play("1 QFT 1 RF 3 QEF")
#print play("1 QFT 1 RF 3 RFE")
#print play("1 QFT 1 RF 3 REF")
#print play("1 QFT 1 RF 3 RQF")
#print play("1 QFT 1 RF 3 RFQ")
#print play("1 AQV 1 QD 10 SEEFWSAQWA")
#print play("1 QFB 1 WF 10 DAEFQQEFWQ")
#print play("1 QWM 1 WD 10 AQRQWQAQWF")
#print play("1 SEV 1 AD 10 SSEQFASRQR")
#print play("1 QRX 1 SF 10 FSDWRRARQQ")
