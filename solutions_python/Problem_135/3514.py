input = [x.strip() for x in open('A-small-attempt0.in', 'r')]
output = open('output.txt', 'w')

case_num = int(input[0])

for i in range(case_num):
    answer1 = int(input[i * 10 + 1])
    cards1 = [int(x) for x in input[i * 10 + 1 + answer1].split(' ')]
    answer2 = int(input[i * 10 + 6])
    cards2 = [int(x) for x in input[i * 10 + 6 + answer2].split(' ')]
    possible_cards = [x for x in cards1 if x in cards2]
    possibilities = len(possible_cards)
    
    output.write("Case #%s: " % (i + 1))
    
    if possibilities == 1:
        output.write("%s" % possible_cards[0])
    elif possibilities > 1:
        output.write('Bad magician!')
    else:
        output.write('Volunteer cheated!')
        
    output.write("\n")




