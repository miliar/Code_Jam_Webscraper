#Jaime Marquinez

def main():
    dic={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
         'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l',
         'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't',
         'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm',
         ' ':' ','\n':'\n','q':'z','z':'q'}
    
    def translate(string):
        translated = str()
        for char in string:
            translated += dic[char]
        return translated
    
    inputFile = open("A-small-attempt0.in.txt",'r')
    outputFile = open("A-small-attempt0.out.txt",'w')
    count = int(inputFile.readline())
    i = 1
    while i <= count:
        outputFile.write('Case #'+str(i)+': '+translate(inputFile.readline().lower()))
        i += 1
    inputFile.close()
    outputFile.close()
    
main()

