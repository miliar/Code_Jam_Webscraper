'''
Created on Apr 13, 2014

@author: adam
'''

in_file = open("A-small-attempt0.in")
out_file = open("A-small-attempt0.out", "w")
num_cases = int(in_file.readline())

for case in range(0, num_cases):
    row_num = int(in_file.readline()) - 1
    cards = []
    for i in range(0,4):
        cards.append(in_file.readline().split())
    first_row = cards[row_num]
    print(first_row)
    row_num = int(in_file.readline()) - 1
    cards = []
    for i in range(0,4):
        cards.append(in_file.readline().split())
    second_row = cards[row_num]
    print(second_row)
    cards = [val for val in first_row if val in second_row]
    print(cards)
    out_str = "Case #" + str((case + 1)) + ": "
    if len(cards) == 1:
        out_str += cards[0]
    elif len(cards) == 0:
        out_str += "Volunteer cheated!"
    else:
        out_str += "Bad magician!"
    out_str += "\n"
    out_file.write(out_str)
    
        

