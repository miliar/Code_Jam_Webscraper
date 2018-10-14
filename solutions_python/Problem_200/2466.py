INPUT_FILE_NAME = "B-large.in"
OUTPUT_FILE_NAME = "B-large.out"

def isTidy(n):
    l = [int(i) for i in str(n)]
    L = len(l)
    for i in range(0, L-1):
        if l[L-i-2] > l[L-i-1]:
            return False, L-i-2
    return True, 0

if __name__ == "__main__":
    inputFile = open(INPUT_FILE_NAME, 'r')
    outputFile = open(OUTPUT_FILE_NAME, 'w')

    numCases = int(inputFile.readline())

    for case in range(0, numCases):
        print("Case #" + str(case+1))
        N = int(inputFile.readline())
        n = N
        tidy = False
        while tidy != True:
            tidy, index = isTidy(n)
            if tidy != True:
                if n > 100:
                    l = list(str(n))
                    l[index+1] = '9'
                    if int(''.join(str(i) for i in l)) > N:
                        l[index] = str(int(l[index])-1)    
                    n = int(''.join(str(i) for i in l))
                else:
                    n = n - 1
        outputFile.write("Case #" + str(case + 1) + ": " + str(n) + "\n")
        print(n)

    print("End")
    inputFile.close()
    outputFile.close()

# outputFile.write("Case #" + str(case) + ": " + str(i+1) + " " + str(j+i+2) + "\n")
