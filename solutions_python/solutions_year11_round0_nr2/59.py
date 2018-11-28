
import sys

def main():

    if len(sys.argv) == 2:
        filename = sys.argv[1] #input file name from command line
    else:
        filename = "testcases.txt"
    inputfile = open(filename, 'r')
    testcases = int(inputfile.readline())
    for i in xrange(testcases):
        print 'Case #%s: %s'%(i+1,jammit(inputfile.readline()))

def jammit(inputline):
#    print inputline,
    datas = inputline.split()
    combocount = int(datas[0])
    anticount = int(datas[combocount+1])
    combos = {}
    antis = {}
    for i in xrange(combocount):
        combo1 = datas[1+i][0]
        combo2 = datas[1+i][1]
        combo3 = datas[1+i][2]
        combos.setdefault(combo1, {})
        combos[combo1][combo2] = combo3
        combos.setdefault(combo2, {})
        combos[combo2][combo1] = combo3

    for i in xrange(anticount):
        anti1 = datas[2+i+combocount][0]
        anti2 = datas[2+i+combocount][1]
        antis.setdefault(anti1, "")
        antis.setdefault(anti2, "")
        antis[anti1] += anti2
        antis[anti2] += anti1
#    print combos
    invokee = datas[-1]
    answer = []
    for i in xrange(len(invokee)):
#        print 'loop', i
        if len(answer) == 0:
            answer = [invokee[i]]
            continue
        #first find match
        try:
            #print 'lookin for combo',invokee[i],answer[-1]
            newb = combos[invokee[i]][answer[-1]]
            answer = answer[:-1] + [newb]
            #print answer, 'through combo application'
        except KeyError:
            answer += [invokee[i]]
            #print answer, 'through combo key error'
            #print 'key error'
        #now check for antis
        
        try:
            for c in antis[answer[-1]]:
                if c in answer:
                    answer = []
                    break
        except KeyError:
            pass
        
 #       print 'temp:', answer

  #  print 'answer',answer
    realanswer = "["
    return "["+', '.join(answer)+"]"
        

        
main()
