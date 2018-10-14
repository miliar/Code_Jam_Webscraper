raw_input = open("A-small-attempt0.in","r").read().split("\n")
test_cases = int(raw_input[0])
test_length = 10
output = ""
for i in range(test_cases):
    input = raw_input[i*test_length+1:i*test_length+test_length+1]
    row1 = int(input[0])
    row2 = int(input[5])
    cards1 = set(input[row1].split(" "))
    cards2 = set(input[5+row2].split(" "))
    final_set = cards1.intersection(cards2)
    if len(final_set)==1:
        answer = final_set.pop()
    elif len(final_set)==0:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"
    output+= "Case #%s: %s\n" % (i+1,answer)
f = open("A-small-attempt.out", "w")
f.write(output)
