import optparse
from string import maketrans

class CodeJamInputFile(object):
    
    def __init__(self, file_name, lines_per_case):
        self.file = open(file_name, 'r')
        self.lines_per_case = lines_per_case
        self.nof_cases = int(self.file.readline().strip("\n\r "))
        
    def __iter__(self):
        return self
    
    def next(self):
        lines = []
        for i in xrange(self.lines_per_case):
            line = self.file.readline()
            
            if len(line) == 0 and i == 0:
                raise StopIteration
            elif len(line) == 0:
                raise Exception("Input error")
            else:  
                lines.append(line.strip("\n\r "))
        
        return lines


if __name__ == "__main__":
    
    parser = optparse.OptionParser()

    parser.add_option("-i", "--in-file", dest="input_file",
                      help="input file")
    parser.add_option("-o", "--out-file", dest="output_file", 
                      help="output file")

    (options, args) = parser.parse_args()

    input = CodeJamInputFile(options.input_file, 1)
    
    intab =  "abcdefghijklmnopqrstuvwxyz"
    outtab = "yhesocvxduiglbkrztnwjpfmaq"
    trantab = maketrans(intab, outtab)
    
    for ix, case in enumerate(input):
        str = case[0]
        out = str.translate(trantab)

        print "Case #%d: %s" % (ix + 1,  out)




