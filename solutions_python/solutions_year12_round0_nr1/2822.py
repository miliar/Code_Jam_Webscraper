## Ronak
## Problem A. Speaking in Tongues
## Start time: 12:40am, Saturday 2012.


def main():

    infile = open("A-small-attempt0.in", "r")

    outfile = open("outputQuali1.txt", "w")

    fileContents =  infile.read().split("\n")
    
    print(fileContents)

    googlerese = {}

    testCases = int(fileContents[0])
    fileContents.remove(fileContents[0])

    print(fileContents)
##    for i in range (int(testCases)):
##
##        for i in range(len(fileContents[0])):
##            #print(fileContents[0][i])
##            
##            if fileContents[0][i] == " ":
##                x = 0
##            elif not googlerese.has_key(fileContents[0][i]):
##                googlerese[fileContents[0][i]] = fileContents[1][i]
##
##                
##        fileContents.remove(fileContents[0])
##        fileContents.remove(fileContents[0])
##        #print fileContents
##
##    
##    googlerese["q"] = "z"
##    googlerese["z"] = "q"
##    print googlerese
##    print len(googlerese.keys())


    googlerese = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

    x = 0
    for i in range(testCases):
        x +=1
        outputStr = ""

        for i in fileContents[0]:
            if i == " ":
                outputStr += " "
            else:
                outputStr = outputStr + googlerese[i]

        fileContents.remove(fileContents[0])

        print outputStr

        outfile.write("Case #" +str(x) + ": " + outputStr + "\n")

main()
