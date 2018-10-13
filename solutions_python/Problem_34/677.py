"""

Author 	: 	Nitin Kumar
email  	: 	nitinkumar810@gmail.com
Date	: 	03rd Sept 2009
Problem	:	Alien Language!

This program creates a dictionary for all the words, then for each test cases, trims the world list as per, valid words for the given case

"""
	
import string

if __name__ == '__main__':

    fin = open('q1.in')         # Opens the input file.. in read mode... must be changed here for different input files..
    fout = open('q1small.out', 'w') # Opens file in write mode for the output of test cases
    count = 1
    List_L = []			# Creates a dictionary for storing all the words of the alien lang
    case = 0			# For keeping track of case no.

    for line in fin:
        word = line.strip()
        line = line.replace('\n','')

        if(count == 1):			# For reading the first line
            L, D, N = line.split()	# Splits the first line and stores in the L, D, N args in string format
            count = count + 1
            continue

        L = int(L)			# For converting L,D,N into numbers)
        D = int(D)
        N = int(N)

	if(count <= D + 1):		# Creates a list containing all the Words of the Alien language
            List_L.append(line);
            count = count + 1
            continue

        temp_line = ''
        check = 0

        for ch in line:			# Following Codes trims and separates all the args for the test cases
            if (ch == '('):
                check = 1
                continue
            if (ch == ')'):
                check = 0
                temp_line = temp_line + ' '
                continue
            if (check == 1):
                temp_line = temp_line + ch
            else:
                temp_line = temp_line + ch + ' '

        temp_line.strip()
        Table_T = temp_line.split(' ')
        Temp_word = ''
        Temp_L_L = List_L
        Temp_L = Temp_L_L

        for i in range(0,len(Table_T) - 1):	#this loop trims the available word list to the possible set of words for the given test case
            Temp_L_L = []
            for ch in Table_T[i]:
                for Temp_L_Data in Temp_L:
                    if ch in Temp_L_Data[i]:
                        Temp_L_L.append(Temp_L_Data)
            Temp_L = Temp_L_L
        
        case = case + 1
        Output_line = 'Case #' + str(case) + ': ' + str(len(Temp_L))  +'\n' #This line creates the output for each particular case... counting the Temp_L containing the possible set of values for the given case

        fout.write(Output_line)
