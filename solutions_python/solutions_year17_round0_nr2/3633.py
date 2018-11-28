import Question2_utils

# case_amount = int(input())
cases = list()
text = ""

with open("B-large.in", "r", encoding='utf-8', errors='ignore') as source:
    for line in source:
        cases.append(line.strip())


for index, e in enumerate(cases[1:]):
    e = Question2_utils.find_tidy(e)
    text += "Case #" + str(index + 1) + ": " + str(e) + "\n"


# print(text)
f = open('result-large', 'w')
f.write(text)