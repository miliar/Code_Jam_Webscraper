def oversizedPancakeFlipperTF(array, k):
    if allHappy(array):
        return 0
    elif k > len(array):
        return None# not possible
    numFlips = 0
    for i in range(len(array)-k+1):
        if array[i] != True:
            numFlips += 1
            for toflip in range(i, i+k):
                array[toflip] = not array[toflip]
    if allHappy(array):
        return numFlips
    else:
        return None
    
    

def allHappy(array):
    for i in range(len(array)):
        if array[i] is not True:
            return False
    return True

def oversizedPancakeFlipper(string, k):
    array = list(string)
    #print(array)
    for i in range(0, len(array)):
        if array[i] == '-':
            array[i] = False
        else:
            array[i] = True
    results = oversizedPancakeFlipperTF(array, k)
    if results == None:
        return 'IMPOSSIBLE'
    else:
        return str(results)

		
		
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  array, k = [s for s in input().split(" ")] 
  results = oversizedPancakeFlipper(array, int(k))
  print("Case #{}: {}".format(i, results))
  # check out .format's specification for more formatting options