inputFile = r"C-small-attempt2.in"
#inputFile = r"Example.in"
#inputFile = r"A-large-practice.in"
outputFile = inputFile.replace("in", "out")    


quaternionMult = {"1": {"1" : "1", "i" : "i",  "j" : "j",  "k" : "k"},
                  "i": {"1" : "i", "i" : "-1", "j" : "k",  "k" : "-j"},
                  "j": {"1" : "j", "i" : "-k", "j" : "-1", "k" : "i"},
                  "k": {"1" : "k", "i" : "j",  "j" : "-i", "k" : "-1"} }


def reducePossible(chars):
    if len(chars) < 3:
        return False
    
    char = chars[0]
    for c in chars:
        if c != char:
            break
    else:
        return False
    
    iSubstrings = findSubstrings(chars, "i", 0, 3)
    
    for subString in iSubstrings:
        jSubstrings = findSubstrings(chars, "j", subString, 2)
        
        for jSubString in jSubstrings:
            kSubStrings = findSubstrings(chars, "k", jSubString, 1)
            if len(kSubStrings) > 0:
                return True
            
    return False
    

def findSubstrings(chars, char, startIndex, rest):
    result = []
    length = 1 + startIndex
    
    while True:
        if chars[startIndex] == char and len(chars) >= startIndex + rest:
            if rest == 1:
                # must be last char
                if len(chars) == startIndex + 1:
                    result.append(length)
                    #yield length
            else:
                result.append(length)
        if len(chars) <= startIndex + rest or len(chars) <= startIndex + 1 + rest and chars[startIndex] == "-":
            return result
            #return
        
        l = len(chars)
        chars = multiply(chars, startIndex)
        newLength = len(chars)
        
        length += l - newLength
        

  
    

def multiply(chars, index):
    minus = 0
    if chars[index] == "-":
        minus += 1
    
    firstChar = chars[index + minus]
    
    if chars[index + 1 + minus] == "-":
        minus += 1
    
    secondChar = chars[index + 1 + minus]
    
    result = ""
    
    if minus % 2 == 1:
        result += "-"
    
    result += quaternionMult[firstChar][secondChar]
    if result[0] == "-" and result[1] == "-":
        result = result[2:]
    return chars[0:index] + result + chars[index + 2 + minus:]
    

def solve(lines):
    numbers = [int(x) for x in lines[0].split()]
    l = numbers[0]
    x = numbers[1]
    # notwendige Bedingung: -1
    chars = lines[1]
    while not (len(chars) == 2 and chars[0] == "-" or len(chars) == 1):
        chars = multiply(chars, 0)
    
    p = x * chars
    while not (len(p) == 2 and p[0] == "-" or len(p) == 1):
        p = multiply(p, 0)

    if p != "-1":
        return "NO"
        
        
    if reducePossible(lines[1]*x):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    lines = open(inputFile, 'r').read().split('\n')
    
    cases = int(lines[0])
    with open(outputFile, 'w') as f:
        for case in range(0,cases):
            print(case)
            startIndex = 2*case  + 1
            solution = solve(lines[startIndex: startIndex + 2])
            caseSolution = "Case #" + str(case + 1) + ": " + solution
            print(caseSolution)
            print(caseSolution, file=f)

    
    
        