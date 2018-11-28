#!/usr/bin/env python

from __future__ import division, print_function


class DigitGetter( object ):
    def __init__( self, inputFile, outFile ):
        self._digitNumberStringPairs = list( enumerate( ( 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE' ) ) )
        self._uniqueLettersToDigits = { 'G': self._digitNumberStringPairs[ 8 ],
                                        'U': self._digitNumberStringPairs[ 4 ],
                                        'W': self._digitNumberStringPairs[ 2 ],
                                        'X': self._digitNumberStringPairs[ 6 ],
                                        'Z': self._digitNumberStringPairs[ 0 ] }
        self._uniqueLettersToDigitsSecondPass = { 'O': self._digitNumberStringPairs[ 1 ],
                                                  'H': self._digitNumberStringPairs[ 3 ],
                                                  'F': self._digitNumberStringPairs[ 5 ],
                                                  'S': self._digitNumberStringPairs[ 7 ] }

        self._digits = []

        with open( inputFile, 'r' ) as i, open( outFile, 'w+' ) as o:
            inputFileContents = i.readlines()
            numberOfCases = inputFileContents[ 0 ]
            for case in inputFileContents[ 1: ]:
                self.getDigits( case )
            self.printDigits( o )

    def getDigits( self, case ):
        digits = []
        case, digits = self._handleNumbersWithUniqueLetters( case, digits, self._uniqueLettersToDigits )
        case, digits = self._handleNumbersWithUniqueLetters( case, digits, self._uniqueLettersToDigitsSecondPass )
        case, digits = self._handleNumbersWithUniqueLetters( case, digits, { 'N': self._digitNumberStringPairs[ 9 ] } )
        digits = sorted( digits )
        self._digits.append( ''.join( map( str, digits ) ) )

    def _handleNumbersWithUniqueLetters( self, case, digits, uniqueLettersToDigits ):
        for letter, digitNumberStringPair in uniqueLettersToDigits.iteritems():
            #print( case, digits )
            findResult = case.find( letter )
            while findResult != -1:
                digits.append( digitNumberStringPair[ 0 ] )
                #print( case, digits )
                for digitLetter in digitNumberStringPair[ 1 ]:
                    case = case.replace( digitLetter, '', 1 )
                #print( case, digits )
                findResult = case.find( letter )

        return case, digits

    def printDigits( self, outputFile ):
        for caseNumber, digits in enumerate( self._digits ):
            print( 'Case #' + str( caseNumber + 1 ) + ': ' + str( digits ), file = outputFile )


if __name__ == '__main__':
    #digitGetter = DigitGetter( 'testInput.txt', 'testOutput.txt' )
    #digitGetter = DigitGetter( 'A-small-attempt0.in', 'results-small.txt' )
    digitGetter = DigitGetter( 'A-large.in', 'results-large.txt' )

