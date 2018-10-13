from re import compile

regex = compile(r"((?:\([a-z]*\))|[a-z])")
subregex = compile(r"([a-z])")

f = open("A-large.in","r")
output = open("A-large.out","w")
data = f.next()[:-1]
data = data.split(" ")
word_length = int(data[0])
words_qty = int(data[1])
cases_qty = int(data[2])
words = []

for word in range(words_qty):
    words.append(f.next()[:-1])
for case_num in range(cases_qty):
    case = f.next()[:-1]
    pattern = []
    matches = regex.findall(case)
    for match in matches:        
        if len(match) > 1:
            pattern.append(subregex.findall(match))
        else:
            pattern.append([match])
    newregex = ""
    for group in pattern:
        newregex += "(?:"
        joiner = ""
        for char in group:
            newregex += joiner+char
            joiner = "|"
        newregex += ")" 
    newregex = compile(newregex)
    matches = 0
    for word in words:
        if newregex.match(word) != None:
            matches += 1
    output.write("Case #"+str(case_num+1)+": "+str(matches)+chr(10))

f.close()
output.close()