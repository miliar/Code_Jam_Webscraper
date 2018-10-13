#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

# AssemblyCompany   = 'Emerging Information Systems Inc.'
# AssemblyTitle     = 'CodeJam2010'
# AssemblyProduct   = 'CodeJam2010'
# AssemblyCopyright = 'Copyright © Emerging Information Systems Inc. 2010'

import sys
import re

output = lambda string: sys.stdout.write( string )

def debug_out( string ):
    #sys.stderr.write( string )
    #sys.stderr.flush()
    pass

def primary_function( instring, **kwargs ):
    """ The Primary function - input a test case as a string, and return the answer string for that test case. """
    inputs = instring.split(' ')
    snappers = int(inputs[0])
    snaps = int(inputs[1])
    debug_out("in: '%s'\na: %d, b: %d\n" % (instring, snappers, snaps))

    x = ( 2 ** snappers )
    required = x - 1
    if snaps > required:
        rounds = snaps / x
        snaps -= rounds * x
    
    if snaps == required:
        return "ON"

    return "OFF"


class Program:
    def main( self, args ):
        if len(args) < 2:
            print("ERROR: Specify input file.")
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
        
        for caseNumber in xrange( 1, numCases + 1 ):
            input_str = textReader.readline().rstrip('\n')
            output_result( primary_function( input_str ) )
        
        textReader.close()
        textWriter.close()


# Run the program is this file is executed (versus imported)
if __name__ == '__main__':
    import sys
    program = Program()
    sys.exit( program.main( sys.argv ) )
