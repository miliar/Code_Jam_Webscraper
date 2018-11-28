
alphabet    = list("abcdefghijklmnopqrstuvwxyz")
translation = list("yhesocvxduiglbkrztnwjpfmaq") # reverse engineered from sample and hint

dictionary = {}

for i in xrange(0, len(alphabet)):
    dictionary[alphabet[i]] = translation[i]

N = int(raw_input())

for case in xrange(0, N):
    translated = []
    sentence = raw_input()
    for char in sentence:
        if char in dictionary:
            translated.append(dictionary[char])
        else:
            translated.append(char)
    print "Case #" + str(case + 1) + ": " + "".join(translated)
        
    

