import math, sys

__author__ = 'Golfpong'

class FairSquare:
    
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)
        self.palindrome = list()

    def get_palindrome(self):
        numbers = range(self.start, self.end+1)

        for number in numbers:            
            if ( str(number) == str(number)[::-1] ):
                root = math.sqrt(number)
                decimal = str(root).split('.')
                
                if ( decimal[1] == '0' and str(int(root)) == str(int(root))[::-1] ):
                    self.palindrome.append(number)
            
    def output(self):
        self.get_palindrome()
        return str(len(self.palindrome))

def run(input_file, output_file):
    file_input = open(input_file)
    file_output = open(output_file, "w")
    case_round = int(file_input.readline())
    for case in range(case_round):
        size = str(file_input.readline()[:-1]).split(" ")
        fs = FairSquare(size[0], size[1])

        output = 'Case #'+str(case+1)+': '+fs.output()+'\n'
        file_output.write(output)

    file_output.write('\n')
        

if __name__ == "__main__":
    #run('C-small-attempt0.in','C-small-attempt0.out')
    run(sys.argv[1], sys.argv[2])
