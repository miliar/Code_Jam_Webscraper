## Google Code Jam contest!
# I need to read a file and save the results in other one.
# The first parameter is the input file name
# The second parameter is the output file name
import sys
import os


pathfile = sys.argv[1]
# outfile = sys.argv[2]
outfile = pathfile.replace('in', 'out')

file_in = open(pathfile, mode='r')
file_out = open(outfile, mode='w')

# First line: number of cases
n_cases = int(file_in.readline())
# Followed by n_cases lines.


class Number:
    def __init__(self, x):
        self.num = x
        self.repr = self.num2list()
        self.tiny = self.is_tiny()

    def __repr__(self):
        return '<Number {} repr: {}>'.format(self.num, self.repr)
    
    def num2list(self):
        return list(map(int, str(self.num)))

    def is_tiny(self):
        i0 = self.repr[0]
        for i in self.repr:
            if i < i0:
                return False
            i0 = i
        return True
    
    def substract1(self):
        self.num -= 1
        self.repr = self.num2list()
        self.tiny = self.is_tiny()

    def substract(self):
        # If we have some zero, substract that position to 9...
        try:
            ind_zero = self.repr[::-1].index(0)
            # that position to the end will be 9s now
            for i in range(len(self.repr)-1-ind_zero, len(self.repr)):
                self.repr[i] = 9

            j = 2
            while len(self.repr)-ind_zero-j >= 0:
                if self.repr[len(self.repr)-j-ind_zero] > 0:
                    self.repr[len(self.repr)-j-ind_zero] -= 1
                    break
                else:
                    self.repr[len(self.repr)-j-ind_zero] = 9
                j += 1

            if self.repr[0] == 0:
                self.repr = self.repr[1:]
            
            temp = 0
            for i, n in enumerate(self.repr):
                temp += n*10**(len(self.repr)-i-1)
            
            self.num = temp
            self.tiny = self.is_tiny()
        except ValueError:
            # No zeros in the number
            self.substract1()



current_case = 0
while current_case < n_cases:
    current_case += 1
    this_case = Number(int(file_in.readline()))
    if this_case.tiny:
        file_out.write('Case #{:d}: {:d}\n'.format(current_case, this_case.num))
    else:
        while not this_case.tiny:
            this_case.substract()

        file_out.write('Case #{:d}: {:d}\n'.format(current_case, this_case.num))


file_in.close()
file_out.close()

