dictionary = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'z': 'q', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

def createDictionary(inputText, outPut):
    outPut = open(outPut)
    inputText = open(inputText)
    cases =  int(inputText.readline())
    
    inLetters = []
    outLetters = []
    for case in range(cases):
        inWords =  inputText.readline()[:-1].split(" ")
        outWords =  outPut.readline()[:-1].split(" ")
        for inWord, outWord in zip(inWords, outWords):
            for inChar, outChar in zip(inWord, outWord):
                if inChar not in inLetters:
                    outLetters.append(outChar)
                    inLetters.append(inChar)
    
    traslator = {'q':'z', ' ':' '}
    for inChar, outChar in zip(inLetters, outLetters):
        traslator[inChar] = outChar

    return traslator


def traslate(inputText):
    outPut = open("output","w")
    inputText = open(inputText)
    cases =  int(inputText.readline())

    for case in range(cases):
        inLine =  inputText.readline()[:-1]
        outLine = ''

        for char in inLine:
            outLine += dictionary[char]      

        outPut.write("Case #"+str(case+1)+": "+ outLine +"\n")      


if __name__ == "__main__":
    b = traslate('A-small-attempt0.in')
    #a = createDictionary("input", "output")
