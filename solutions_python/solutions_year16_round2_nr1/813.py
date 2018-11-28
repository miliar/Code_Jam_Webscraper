def number(s):
    identifiers_first_round={"Z" : "ZERO", "W" :"TWO", "U":"FOUR", "X":"SIX", "G":"EIGHT"}
    identifiers_second_round={"O": "ONE", "H":"THREE","F":"FIVE", "S":"SEVEN"}
    identifiers_last ={"I":"NINE"}
    number_dict={"Z":"0", "W":"2", "U":"4","X":"6","G":"8", "O":"1", "H":"3", "F":"5", "S":"7","I":"9"}
    numberp=""
    for key in identifiers_first_round.keys():
        if key in s:
            occurence = s.count(key)
            for char in identifiers_first_round[key]:
                s = s.replace(char,'',occurence)
            numberp = numberp + number_dict[key]*occurence
    for key in identifiers_second_round.keys():
        if key in s:
            occurence = s.count(key)
            for char in identifiers_second_round[key]:
                s = s.replace(char,'',occurence)
            numberp = numberp + number_dict[key]*occurence
    for key in identifiers_last.keys():
        if key in s:
            occurence = s.count(key)
            for char in identifiers_last[key]:
                s = s.replace(char,'',occurence)
            numberp = numberp + number_dict[key]*occurence
    numberp = ''.join(sorted(numberp))
    return numberp




solution = open('solution.txt', 'w')
with open('test.txt') as f:
    N= int(f.readline())
    count = 1
    for line in f:
        lastWord= number(line)
        newLine = 'Case #'+ str(count) +': '+ lastWord +'\n'
        solution.write(newLine)
        count +=1

