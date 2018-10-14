Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
T = int(InputList[0])
InputList.pop(0)
OutputList = []
Consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
for case in range(T):
    name = InputList[case].split()[0]
    n = int(InputList[case].split()[1])
    nvalue = 0
    substrings=[ name[ index : index + length ] for index in range( len( name ) - 1 ) for length in range( 2, len( name ) - index + 1 ) ]
    for substring in substrings:
        consonantsLen = 0
        for character in substring:
            if character in Consonants:
                consonantsLen += 1
                if consonantsLen >= n:
                    nvalue += 1
                    break
            else:
                if consonantsLen >= n:
                    nvalue += 1
                    break
                else:
                    consonantsLen = 0
    OutputList.append("Case #" + str(case + 1) + ": " + str(nvalue))


Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()