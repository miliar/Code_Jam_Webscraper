import string

info = open("C:\\CodeJam\\QualificationInfo.txt")
file = open("C:\CodeJam\\QualificationA.in","r")
output = open("C:\CodeJam\\QualificationA.txt","w")

infoText = info.read().split("\n\n")
encoded, decoded = infoText[0].strip(), infoText[1].strip()
modifier = {"a":"y","o":"e","z":"q"}

for charIndex in range(len(encoded)):
    encodedLetter = encoded[charIndex].lower()
    decodedLetter = decoded[charIndex].lower()
    if encodedLetter in string.ascii_letters:
        modifier[encodedLetter] = decodedLetter

for letter in string.ascii_letters:
    if letter not in modifier.keys():
        if letter.isupper():
            modifier[letter] = modifier[letter.lower()].upper()
        else:
            for decode in string.ascii_lowercase:
                if decode not in modifier.values():
                    modifier[letter] = decode
                    break

cases = int(file.readline())

for case in range(1,cases+1):
    caseText = file.readline().strip()
    decodedLine = ""
    for letter in caseText:
        if letter in modifier.keys():
            decodedLine += modifier[letter]
        else:
            decodedLine += letter
    output.write("Case #" + str(case) + ": " + decodedLine)
    if case != cases:
        output.write("\n")

info.close()
file.close()
output.close()