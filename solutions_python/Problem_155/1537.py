
inName = "A-large.in"
outName = "output.txt"

def determine_min_persons(shyString):
    required = 0
    peopleCount = 0
    shyCount = 0
    for num in shyString:
        num = int(num)
        #print(peopleCount, shyCount)
        if shyCount > peopleCount:
            required += shyCount - peopleCount
            peopleCount += shyCount - peopleCount
        
        peopleCount += num
        shyCount += 1
    return required

if __name__ == "__main__":
    outFile = open(outName, 'w')
    results = ""
    
    with open(inName, 'r') as f:
        cases = int(f.readline())
        for i in range(0, cases):
            maxShy, shyString = f.readline().split(" ")
            maxShy = int(maxShy)
            minPersons = determine_min_persons(shyString[0:maxShy+1])
            results += "Case #{}: {}\n".format(i + 1, minPersons)
            
    results.strip()
    outFile.write(results)
    outFile.close()
    print(results)
    print("Operation complete")