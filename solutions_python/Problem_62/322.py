#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

# AssemblyCompany   = 'Emerging Information Systems Inc.'
# AssemblyTitle     = 'CodeJam2010'
# AssemblyProduct   = 'CodeJam2010'
# AssemblyCopyright = 'Copyright © Emerging Information Systems Inc. 2010'

import sys
import re
import operator

output = lambda string: sys.stdout.write( string ) and sys.stdout.flush()

def debug_out( string ):
    if False:
        sys.stderr.write( string )
        sys.stderr.flush()
    pass

def primary_function( wirelist ):
    """ The Primary function - input a test case as a string, and return the answer string for that test case. """
    debug_out('\n')

    wirelist = sorted( wirelist, key=operator.itemgetter(0) )
    debug_out('sorted: %s\n' % wirelist )

    total_crossings = 0
    
    while len(wirelist) > 1:
        a, b = wirelist[0]
        
        crosses = 0
        crossings = [ xy for xy in wirelist[1:] if xy[1] < b ]
        debug_out('  %s, %s \tcrossings: %s\n' % (a, b, crossings,) )
        total_crossings += len(crossings)

        wirelist = wirelist[1:]
    
    return total_crossings


class Program:
    def main( self, args ):
        if len(args) < 2:
            print("ERROR: Specify input file...")
            return 1
        else:
            INPUT_FILE = args[1]
            OUTPUT_FILE = re.sub('(.*)[.]in', '\\1.out', INPUT_FILE)

        textReader = open(INPUT_FILE,  'r')
        textWriter = open(OUTPUT_FILE, 'w')

        def output_result( answer ):
            output('Case #%d: %s\n' % (caseNumber, answer))
            textWriter.write('Case #%d: %s\n' % (caseNumber, answer))

        numCases = int( textReader.readline() )  # get the first line
        output("Found %d cases..\n" % numCases)
        
        # Parse the input and run one test case at a time
        for caseNumber in range( 1, numCases + 1 ):
            num_wires = int( textReader.readline().rstrip('\n'), 10 )
            wirelist = []
            for i in range( 1, num_wires + 1 ):
                x, y = textReader.readline().rstrip('\n').split(' ')
                wirelist.append( (int(x,10), int(y,10)) )

            #debug_out('wirelist: %s' % wirelist)
            
            output_result( primary_function( wirelist ) )
            
        
        textReader.close()
        textWriter.close()


# Run the program is this file is executed (versus imported)
if __name__ == '__main__':
    import sys
    program = Program()
    sys.exit( program.main( sys.argv ) )
