import sys
import pdb
sys.path.append('D:/codejam/qualification round/C')

file = open('input.txt')
input = file.read()
file.close()

input = input.split("\n")

T = int(input[0])
input = input[1:]

result = []

def number_of_digits(x):
    i = 0
    while True:
        if x < 10**i:
            break
        else:
            i += 1
    return i
        
for i in range(0,T):
    A, B = int(input[0].split(' ')[0]), int(input[0].split(' ')[1])
    recycles = 0
    for n in range(A,B):
        for j in range(1,number_of_digits(n)):
            m = n/(10**j) + (10**(number_of_digits(n)-j)) * ( n%(10**j) )
            #pdb.set_trace()
            if m > n and m <= B:
                recycles += 1
    result += [recycles]
    input = input[1:]
    
file = open('output.txt', 'w')
for i in range(0,T):
    file.write( "Case #" + str(i+1) + ": " + str(result[i]) + "\n" )
file.close()