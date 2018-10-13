input_file = open('A-small-attempt0.in')
output_file = open('output.txt', 'w')
tests = int(input_file.readline()[:-1])
for test in range(tests):
    answer = int(input_file.readline()[:-1])
    cards = []
    for i in range(4):
        cards.append({int(j) for j in input_file.readline()[:-1].split()})
    set_one = cards[answer-1]
    answer = int(input_file.readline()[:-1])
    cards = []
    for i in range(4):
        cards.append({int(j) for j in input_file.readline()[:-1].split()})
    set_two = cards[answer-1]
    user_card = list(set_one & set_two)
    if user_card:
        if len(user_card) == 1:
            output_file.write('Case #'+str(test+1)+': '+str(user_card[0])+'\n')
        else:
            output_file.write('Case #'+str(test+1)+': '+'Bad magician!\n')
    else:
        output_file.write('Case #'+str(test+1)+': '+'Volunteer cheated!\n')
input_file.close()
output_file.close()