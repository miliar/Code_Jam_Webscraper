f = open("A-small-attempt1.in")
strings = f.readlines()
f.close()

NumberTestCases = int(strings[0]) #get the number of test cases from first element

strings.pop(0)

lettersTranslation = {
'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q'
}

Output=open("speakingOutput.txt","w") # 
caseNumber = 1
for string in strings:
    str = string.split(' ')
    translation = []
    for word in str:
        letters = list(word)
        translatedChacs = ""
        for character in letters:
            if(character != '\n'):
                translatedCharacter = lettersTranslation[character]            
                translatedChacs += translatedCharacter
    
        translation.append(translatedChacs)
    
    tSentence = ' '.join(translation)
    
    print("Case #%d: %s"%(caseNumber, tSentence,))
    Output.write("Case #%d: %s\n"%(caseNumber, tSentence,))  
    caseNumber += 1      

Output.close