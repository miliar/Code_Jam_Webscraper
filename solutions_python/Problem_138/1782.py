import copy
with open ("D-small-attempt0.in", "r") as problem:
    problem_text=problem.read()
lines = problem_text.split('\n')
cases = int(lines[0])
#Noami = [0.186,0.389,0.907,0.832,0.959,0.557,0.300,0.992,0.899]
#Ken = [0.916,0.728,0.271,0.520,0.700,0.521,0.215,0.341,0.458]
fo = open('problem-D.out', 'w')
def outfile(text):
    fo.write (text+"\n")

def War(NoamiBlocks,KenBlocks):
    NoamiScore = 0
    for woods in range(0,len(KenBlocks)):
        KenBlocks.sort()
        NoamiBlocks.sort()
        NoamiSelected = NoamiBlocks[0]
        KenSelected = KenBlocks[0]
        for i in range (0,len(KenBlocks)):
            if ( float(KenBlocks[i]) > float(NoamiSelected) ):
                KenSelected =  KenBlocks[i]
                break
        if ( float(KenSelected) < float(NoamiSelected) ):
            NoamiScore += 1
        KenBlocks.remove(KenSelected)
        NoamiBlocks.remove(NoamiSelected)
    return NoamiScore

def DeceitfulWar(NoamiBlocks,KenBlocks):
    NoamiScore = 0
    for woods in range(0,len(KenBlocks)):
        KenBlocks.sort()
        NoamiBlocks.sort()
        if ( NoamiBlocks[len(NoamiBlocks)-1] > KenBlocks[len(KenBlocks)-1]):
            NoamiTold = NoamiBlocks[len(NoamiBlocks)-1]
            NoamiSelected = NoamiBlocks[len(NoamiBlocks)-1]
        else:
            NoamiSelected = NoamiBlocks[0]
            NoamiTold = float(KenBlocks[len(KenBlocks)-1]) - 0.0000001
        KenSelected = KenBlocks[0]
        for i in range(0,len(KenBlocks)):
            if (float(KenSelected) < float(NoamiTold) ):
                KenSelected = KenBlocks[i]
        if ( float(KenSelected) < float(NoamiSelected) ):
            NoamiScore += 1
        KenBlocks.remove(KenSelected)
        NoamiBlocks.remove(NoamiSelected)
    return NoamiScore

for i in range(0,cases*3,3):
    line_number = i+1
#    numberOfWoods = float(lines[line_number])
    woodsNoami = lines[line_number+1].split(' ')
    woodsKen = lines[line_number+2].split(' ')
    woodsNoami2 = copy.copy(woodsNoami)
    woodsKen2 = copy.copy(woodsKen)
    outfile("Case #"+str(int((i/3)+1))+": "+str(DeceitfulWar(woodsNoami2,woodsKen2))+" "+str(War(woodsNoami,woodsKen)))
################################################ I/O
fo.close()
################################################ I/O
