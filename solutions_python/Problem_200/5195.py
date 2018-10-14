import sys

#------------------------------------------------------------------------------------------
def isValid(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return -1
    return 1     
#------------------------------------------------------------------------------------------
def makeTidy(numbers):
    ans = []
    while(True):
        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                ans.append(numbers[i])
            else:
                ans.append(numbers[i]-1)
                for j in range(i,len(numbers)-1):
                    ans.append(9)
                break
        if isValid(ans) == 1:
            return ans
#------------------------------------------------------------------------------------------
def merge(arr): 
    s = ""
    for i in arr:
        s = s + str(i)
    if s[0] == "0":
        s = s[1:]
    return s
#------------------------------------------------------------------------------------------
if __name__ == '__main__':

    data   = [line.rstrip('\n') for line in open(sys.argv[1])]
    output = open ( sys.argv[2] , 'w' )

    data = data[1:]
    row = 1
    for item in data: 
        numbers = [int(i) for i in str(item)]
        if len(numbers) == 1: 
            output.write("Case #" + str(row) + ": " + merge(numbers) + "\n" )
        else: 
            if isValid(numbers) == 1 :
                output.write("Case #" + str(row) + ": " + merge( numbers ) + "\n" )
            else:
                output.write("Case #" + str(row) + ": " + merge(makeTidy(numbers)) + "\n" )
        row += 1
    output.close()
