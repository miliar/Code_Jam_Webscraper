'''
Created on 8 apr. 2017

@author: windows7
'''
def calcRowOne(rowPancakes, thisFlipper):
    flips = 0
    position = 0
    solution = "IMPOSSIBLE"
    facit = ""
    listPancakes = list(rowPancakes)
    for pancakeNr in range(0,len(rowPancakes)):
        newRow = "" 
        facit = facit + "+"                                                       
        if (rowPancakes[pancakeNr] == "-"):
            if ((position + int(thisFlipper)) <= len(rowPancakes)): 
                temp = rowPancakes[position:position + int(thisFlipper)].replace("+", "*")
                temp = temp.replace("-", "+")
                temp = temp.replace("*", "-")
                listPancakes[position:position + int(thisFlipper)] = temp
                flips+=1
                
        position+=1
        rowPancakes = "".join(listPancakes)
    if (rowPancakes == facit):
        solution = str(flips)
    return solution


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
 
    
    for i in range(1, t + 1):
        pancakes, sizeFlipper = [s for s in input().split(" ")]  # read a list of integers, 2 in this case    
        minFlips = calcRowOne(pancakes, sizeFlipper)
        print("Case #{}: {}".format(i, minFlips))

    
#     

#             
