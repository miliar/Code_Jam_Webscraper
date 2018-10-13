#!/usr/bin/python3

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

path="/Users/Cristian/Documents/Maratones y Prácticas/Google Code Jam/2017/ProblemA.out"
with open(path, "w") as file:
    file.write("")

debug=False

def pout(string):
    if(debug):
        print(string)
    else:
        with open(path, "a") as file:
            file.write(string+"\n")
#-------------------------------------------------------------------------------
#   Problem C. Bathroom Stalls
#-------------------------------------------------------------------------------

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    row, K = input().split(" ")
    L = len(row)
    K = int(K)
    answer = '+'*L
    if row == answer:
        pout("Case #{}: {}".format(i, 0))
    elif K == len(row) and row == '-'*K:
        pout("Case #{}: {}".format(i, 1))
    else:
        # Thinking
        tree = [(row, 1)]
        dictionary = {}
        findSolution = False
        levelFinal = -1

        while not findSolution and tree:
            (row, level) = tree.pop(0)
            for c in range(0, L - K + 1):
                rowCopy = ''
                for j in range(0, L):
                    if j>=c and j<c+K:
                        if row[j] == '+':
                            rowCopy = rowCopy + '-'
                        else:
                            rowCopy = rowCopy + '+'
                    else:
                        rowCopy = rowCopy + row[j]

                if rowCopy == answer:
                    levelFinal = level
                    findSolution = True
                elif not rowCopy in dictionary:
                    tree.append((rowCopy, level+1))
                    dictionary[rowCopy] = True
            #print(tree)

        if findSolution:
            pout("Case #{}: {}".format(i, levelFinal))
        else:
            pout("Case #{}: IMPOSSIBLE".format(i))

    # check out .format's specification for more formatting options
