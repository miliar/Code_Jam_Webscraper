import sys

def subLetters(message):
    newMessage = ""
    for element in range(0, (len(message))):
        newMessage += {
            'a': 'y',
            'b': 'h',
            'c': 'e',
            'd': 's',
            'e': 'o',
            'f': 'c',
            'g': 'v',
            'h': 'x',
            'i': 'd',
            'j': 'u',
            'k': 'i',
            'l': 'g',
            'm': 'l',
            'n': 'b',
            'o': 'k',
            'p': 'r',
            'q': 'z',
            'r': 't',
            's': 'n',
            't': 'w',
            'u': 'j',
            'v': 'p',
            'w': 'f',
            'x': 'm',
            'y': 'a',
            'z': 'q',
            '\n': '',
            ' ': ' '}[message[element]]
    return newMessage

def getAnswers():
    filename = input()
    fileStream = open(filename)
    message = fileStream.readlines()
    out = open("outFile2.out", 'w')
    for x in range(1, int(message[0])+1):
        case = "Case #" + str(x) + ": " + subLetters(message[x]) + '\n'
        print(case)
        out.write(case)
    out.close
    
        
if __name__ == "__main__":
    getAnswers()
    
