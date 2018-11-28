'''
Created on Apr 13, 2012

@author: conan
'''

from __future__ import print_function
from root.myStartup import findFile
import sys
from os import chdir, getcwd, remove, rename, listdir, path


#===============================================================================
# import numpy 
# a = numpy.array([
# [1, 2],
# [1, 2]
#               ])
# 
# b = numpy.array([
# [1, 2],
# [1, 2]
#               ])
# 
# x = numpy.linalg.solve(a, b)
#===============================================================================



#change current working directory
CWD = path.abspath('C:/Users/conan/eclipseProjects/myPyLib/src/root/codejam/')
DESKTOP_DIR = path.abspath('C:/Users/conan/Desktop/')
chdir(CWD)
if getcwd() != CWD:
    print('Warning:current directory is not codejam', file=sys.stderr)

def cleanUp():
    files = findFile('\.in$')
    print ('Delete files %s ?' % files)
    if raw_input('[y/n]') == 'y' or 'Y':
        for f in files:
            remove(f)

def cutPaste():
    '''
    After downloading the .in file to the desktop.
    Call this function to cut and paste the file to the codejam directory.
    '''
    for basename in listdir(DESKTOP_DIR):
        if basename.endswith('.in'):
            Origin, New = path.join(DESKTOP_DIR, basename), path.join(CWD, basename)
            rename(Origin, New)
            print('Cut and Paste:"%s" ---> "%s"' % (Origin, New))
            return basename
    return None

def test(solve, inputObj, outStream='output.out'):
    '''
    Applying the function solve to each case in the input object created from 
    the input file.
    '''
    #print to file or to stdout
    outStream = outStream and open(path.join(CWD, outStream), 'w') or sys.stdout
    for caseNum in range(inputObj.numCases):
        print ('Case #%d: %s' % (caseNum + 1, solve(inputObj)), file=outStream)
    print('Output generated to file "%s"' % outStream)



class Problem(object):
    def __init__(self, letter, sampleInputStr):
        self.letter = letter
        self.sampleInputObj = Input(sampleInputStr)
        self.smallInputObj = None
        self.largeInputObj = None
    
    def solve(self, inputObj):
        '''Note that this function only has to solve one case. Use test() to solve
        the whole input'''
        #handle the input accordingly
        raise NotImplementedError
     
    
    def interact(self, opt=None):
        '''
        1. test on the sample input
            if correct: download the input and produce the output
            if incorrect: terminate
        2. multiple the small input by n to test the performance of the large input
        3. if large output is produced within 8 minutes, then download the large input
        and test
        '''
        assert self.sampleInputObj, 'sample input not found'
        #this prints results to the console
        
        while(1):
            option = opt or int(raw_input(
                           'You may choose one of the following:\n'
                           '1: Test on sample input\n'
                           '2: Solve small input\n'
                           '3: Solve fake large input\n'
                           '4: Solve real large input\n'
                           '5: Exit\n'))
            if option == 1:
                #sample
                self.sampleInputObj.reset()
                test(self.solve, self.sampleInputObj, None)
            elif option == 2:
                #small
                print('Now download the small input file and press enter')
                raw_input()
                self.smallInputObj = Input(cutPaste() or findFile(r'small.*?\.in$', '.', 1)[0])
                assert self.smallInputObj, 'small input invalid'
                test(self.solve, self.smallInputObj, '%s-small-output.txt' % self.letter)
            elif option == 3:
                #fake
                n = int(raw_input('Generate fake large input by copying small input n times. Choose n:\n'))
                self.largeInputObj = self.smallInputObj * n
                ##time the procedure
                test(self.solve, self.largeInputObj, '%s-large-test.txt' % self.letter)
            elif option == 4:
                #large
                print('Now download the small input file and press enter')
                raw_input()
                self.largeInputObj = Input(cutPaste() or findFile(r'large.*?\.in$', '.', 1)[0])
                test(self.solve, self.largeInputObj, '%s-large-output.txt' % self.letter)
            else:
                return
        
        
        

class Input(object):
    def __init__(self, inputSrc):
        '''
        @param inputSrc: either a filename containing the input such as 'B-small.in'
        or pass a sample input 
        '''
        if inputSrc.endswith('.in'):
            f = open(path.join(CWD, inputSrc))
            inputSrc = f.read()
            f.close()
        #usually the first line is the number of cases
        self.numCases, self.full_body_text = inputSrc.split('\n', 1)
        self.numCases = int(self.numCases)
        self.reset()
         
    
    def __repr__(self):
        return '%d\n%s' % (self.numCases, self.full_body_text)
    
    def __mul__(self, other):
        assert isinstance(other, int), 'Input object can only be multiplied by an integer'
        return Input('%d\n%s' % (self.numCases * other, self.full_body_text * other))
    
    def reset(self):
        self.iterator = iter(self.full_body_text.splitlines())
        
    def nextLine(self, sep=None, toInt=False, toFloat=False):
        '''
        If sep is specified, then return the line is splitted to a list.
        If toInt is true, then each element is converted to an integer.
        The returned line may be part of a single case.
        '''
        line = ''
        while (line == ''):
            line = self.iterator.next()
        if sep is not None: 
            line = line.split(sep)
        if toInt: 
            assert set is not None, 'Line must be splitted first'
            line = map(int, line)
        if toFloat:
            line = map(float, line)
        return line
  
if __name__ == '__main__':
    pass
