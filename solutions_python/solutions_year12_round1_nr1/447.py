'''
I have a really long password, and sometimes I make a mistake when I type it. Right now I've typed part of my password, but I might have made some mistakes. In particular, I might have pressed the wrong key while typing one or more of the previous characters. Given how likely I was to get each character right, what should I do?

I have three options:

Finish typing the password, then press "enter". I know I'll type the rest of the characters perfectly. If it turns out that one of the earlier characters was wrong, I'll have to retype the whole thing and hit "enter" again -- but I know I'll get it right the second time.
Hit "backspace" some number of times, deleting the last character(s) I typed, and then complete the password and press "enter" as in option 1. If one of the characters I didn't delete was wrong, I'll have to retype the whole thing and press "enter", knowing I'll get it right the second time.
Give up by pressing "enter", retyping the password from the start, and pressing "enter" again. I know I'll get it right this time.
I want to minimize the expected number of keystrokes needed. Each character in the password costs 1 keystroke; each "backspace" costs 1 keystroke; pressing "enter" to complete an attempt or to give up costs 1 keystroke.

Note: The "expected" number of keystrokes is the average number of keystrokes that would be needed if the same situation occurred a very large number of times. See the example below.

Example

Suppose my password is "guest" and I have already typed the first two characters, but I had a 40% chance of making a mistake when typing each of them. Then there are four cases:

I typed "gu" without error. This occurs with probability 0.6 * 0.6 = 0.36.
I typed the 'g' correctly but I made a mistake typing the 'u'. Then I have two letters typed still, but the second one is wrong: "gX". (Here, the 'X' character represents a mistyped letter.) This occurs with probability 0.6 * 0.4 = 0.24.
I typed the 'u' correctly but I made a mistake typing the 'g': "Xu". This occurs with probability 0.4 * 0.6 = 0.24.
I made a mistake typing both letters, so I have two incorrect letters: "XX". This occurs with probability 0.4 * 0.4 = 0.16.
I don't know how many mistakes I actually made, but for any strategy, I can calculate the expected number of keys required to use it. This is shown in the table below:

"gu"   	"gX"   	"Xu"   	"XX"   	Expected
Probability	0.36	0.24	0.24	0.16	-
Keystrokes if I keep typing	4	10	10	10	7.84
Keystrokes if I press backspace once	6	6	12	12	8.4
Keystrokes if I press backspace twice  	8	8	8	8	8
Keystrokes if I press enter right away	7	7	7	7	7
If I keep typing, then there is an 0.36 probability that I will need 4 keystrokes, and an 0.64 probability that I will need 10 keystrokes. If I repeated the trial many times, then I would use 4 keystrokes 36% of the time, and 10 keystrokes the remaining 64% of the time, so the average number of keystrokes needed would be 0.36 * 4 + 0.64 * 10 = 7.84. In this case however, it is better to just press enter right away, which requires 7 keystrokes.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing two integers, A and B. A is the number of characters that I have already typed, and B is the total number of characters in my password.

This is followed by a line containing A real numbers: p1, p2, ..., pA. pi represents the probability that I correctly typed the ith letter in my password. These real numbers will consist of decimal digits and at most one decimal point. The decimal point will never be the first or the last character in a number.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the expected number of keystrokes I need, assuming I choose the optimal strategy. y must be correct to within an absolute or relative error of 10-6.

Limits

1 = T = 20.
0 = pi = 1 for all i.

Small dataset

1 = A = 3.
A < B = 100.
Large dataset

1 = A = 99999.
A < B = 100000.
Sample


Input 
 	
Output 
 
3
2 5
0.6 0.6
1 20
1
3 4
1 0.9 0.1
Case #1: 7.000000
Case #2: 20.000000
Case #3: 4.500000
'''

import os
import itertools

#---------------------------------------------------------------------
# Return a list of all combinations
#---------------------------------------------------------------------
def Combinations(A):
    array = []
    for i in range(A):
        array.append(1)
        array.append(0)
    
    outlist = []
    for element in list(itertools.permutations(array, A)):
        if element not in outlist:
            outlist.append(element)
    
    return outlist

#---------------------------------------------------------------------
# Keystrokes if keep typing
#---------------------------------------------------------------------
def KeystrokesTyping(A, B, P):
    total = 0
    
    for element in Combinations(A):
        prob = Probability(element, P)
        if prob != 0.0:
            if 1 not in element:
                temp = prob * (int(B) - int(A) + 1)
                total += temp
            else:
                temp = prob * (int(B) - int(A) + 2 + int(B))
                total += temp
                
    return total

#---------------------------------------------------------------------
# Keystrokes if backspace
#---------------------------------------------------------------------
def KeystrokesBackspace(A, B, P, num):
    total = 0
    
    newP = []
    for i in range(num):
        newP.append(P[i])
    
    for element in Combinations(int(A) - num):
        prob = Probability(element, P)
        if prob != 0.0:
            if 1 not in element:
                temp = prob * (int(B) - int(A) + 1 + 2 * num)
                total += temp
            else:
                temp = prob * (int(B) - int(A) + 2 + int(B) + 2 * num)
                total += temp
                
    return total
    
#---------------------------------------------------------------------
# Combined probability for current attempt
#---------------------------------------------------------------------
def Probability(list, P):
    res = 1.0

    for i in range(len(list)):
        if list[i] == 0:
            res = res * float(P[i])
        if list[i] == 1:
            res = res * (1.0 - float(P[i]))
    return res
    
#---------------------------------------------------------------------
# Load text file and buffer into a list
#---------------------------------------------------------------------
def LoadFile(filename):
    array = []

    with open(filename, "r") as f:
        for line in f:
            array[len(array):] = [line]
    
    return array
    
#---------------------------------------------------------------------
# Main
#---------------------------------------------------------------------
def main():
    array = LoadFile("Problem 1.txt")
    
    if len(array) > 1:
        solution = ""
        casenum = 1
        
        for i in range(1, len(array), 2):
            partialsolutions = []
            
            dataset = array[i].split()
            
            A = int(dataset.pop(0))
            B = int(dataset.pop(0))
            
            P = array[i+1].split()
            
            partialsolutions.append(KeystrokesTyping(A, B, P))
            
            for i in range(1, A + 1):
                partialsolutions.append(KeystrokesBackspace(A, B, P, i))
                
            partialsolutions.append(B + 2)
            
            partialsolutions.sort()
            
            solution += "Case #" + str(casenum) + ": " + '%.6f' %partialsolutions[0] + '\n'
            casenum = casenum + 1
            
            print >> open("Problem 1 Output.txt", "w"), solution
    
    os.system('pause')

#---------------------------------------------------------------------
# MAIN ENTRY POINT
#---------------------------------------------------------------------
if __name__ == "__main__":
    main()