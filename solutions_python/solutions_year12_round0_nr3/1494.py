#!/usr/bin/python
# -*- coding: utf-8 -*-


FILENAME = r'q2.txt'

class Program:
    def main( self, args ):

        textReader = open('%s'  % (FILENAME,), 'r')
        textWriter = open('%s_out.txt' % (FILENAME,), 'w')

        numCases = int( textReader.readline() )

        for caseNumber in range( 1, numCases + 1 ):
            print(caseNumber)
            nums = [int(x) for x in textReader.readline().strip().split(' ')]
            a = nums[0]
            b = nums[1]
            result = 0
            seen = {}
            for i in range(a, b):
                target = str(i)
                for ix in range(1, len(target)):
                    tmp = int(target[ix:]+target[0:ix])
                    if i<tmp and tmp <=b:
                        pair = (i,tmp)
                        if pair not in seen:
                            result += 1
                            seen[pair] = 1

            textWriter.write('Case #%d: %s\n' % (caseNumber, str(result)))
            #textWriter.write('Case #%d: %s\n' % (caseNumber, str(len(res))))

        textReader.close()
        textWriter.close()


# Run the program is this file is executed (versus imported)
if __name__ == '__main__':
    import sys
    program = Program()
    sys.exit( program.main( sys.argv ) )
