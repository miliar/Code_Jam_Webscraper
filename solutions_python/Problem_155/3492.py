lines = [line.strip() for line in open('test.txt')]
i = 1
case = []
while i < len(lines):
    case.append(lines[i].split(" ")[1])
    i = i + 1

#print(case)

def test(ppl):
    clap = int(ppl[0])
    total = int(ppl[0])
    i = 1
    while i < len(ppl):
        if clap >= i:
            clap = clap + int(ppl[i])
        total = total + int(ppl[i])
        i = i + 1
    if clap == total:
        return True
    else:
        return False

solution = []

for audience in case:
    invite = 0
    while not test(audience):
        audience_list = list(audience)
        audience_list[0] = str(int(audience_list[0])+1)
        invite = invite + 1
        audience = "".join(audience_list)
    solution.append(invite)

i = 1
for lines in solution:
    print("Case #"+ str(i) + ": " +str(lines))
    i = i +1
