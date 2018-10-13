import os,sys
import logging

logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

infilename = sys.argv[1]
#infilename = 'MTdemo.in'
outfilename = 'MagicTrick.out'

outfile = open(outfilename,'w')


linenum =0
testcase = 0
rownum = 4
casenum = 0


with open(infilename,'rb') as f:
    testcase = f.readline()
    logging.debug('how many testcase:')
    logging.debug(testcase)    
    testcase = int(testcase)
    #every case
    while casenum < testcase:
        first_chose = f.readline()
        logging.debug('first chose:')
        logging.debug(first_chose)
        first_chose = int(first_chose) - 1
        
        totalrow = 0

        while totalrow < rownum:
            line=f.readline()
            logging.debug('first assignment:')
            logging.debug(totalrow)
            #process each line
            if totalrow == first_chose:

                logging.debug(line)
                first_choseline = line
                first_choseline = first_choseline.split()
                logging.debug(first_choseline)
                               
            totalrow += 1

        second_chose = f.readline()
        logging.debug('second chose:')
        logging.debug(second_chose)
        second_chose = int(second_chose) - 1

        totalrow = 0
        while totalrow < rownum:
            line=f.readline()
            logging.debug('second assignment:')
            logging.debug(totalrow)
            #process each line
            if totalrow == second_chose:
                logging.debug(line)
                second_choseline = line
                second_choseline = second_choseline.split()
                logging.debug(second_choseline)
            totalrow += 1
                                
        howtime = 0
        answer = 0
        for second_item in second_choseline:
            if second_item in first_choseline:
                howtime += 1
                answer = second_item
        
        logging.debug('judgement:')    
        newlinum = casenum + 1
        if howtime == 0:
            print 'Case #%d: Volunteer cheated!'  % newlinum
            outfile.write('Case #%d: Volunteer cheated!\n'  % newlinum)
        elif howtime == 1:
            print 'Case #%d: %s' %(newlinum,answer)
            outfile.write('Case #%d: %s\n'  % (newlinum,answer) )
        elif howtime > 1:
            print 'Case #%d: Bad magician!'  % newlinum
            outfile.write('Case #%d: Bad magician!\n'  % newlinum )
        casenum += 1


outfile.close()
