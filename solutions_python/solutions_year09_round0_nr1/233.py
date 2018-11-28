import sys
import re

def main(argv):
    ifilename = argv[1]
    ofilename = argv[2]
    ifile = open(ifilename, 'r')
    numlines = ifile.readline()
    ofile = open(ofilename, 'w')
    args = numlines.split(" ");
    for i in range(len(args)):
        args[i] = int(args[i])
    L,D,N = args
    
    words = []
    for i in range(D):
        words.append(ifile.readline().strip())
        
    dictionary = set(words)
        
    for i in range(N):
        number = numberWords(ifile.readline().strip(), dictionary)
        ofile.write("Case #"+str(i+1)+": "+str(number)+"\n")
    
    ifile.close()
    ofile.close()
    
def numberWords(testWord, dictionary):
    testWord = testWord.replace("(","[")
    testWord = testWord.replace(")","]")
    exp = re.compile(testWord)
    number = 0
    for word in dictionary:
        result = exp.match(word)
        if result is not None:
            number += 1
    return number
    
if __name__ == '__main__':
    main(sys.argv)