#!/usr/bin/python

def magic_trick(cards, selections):
    selected_cards = []
    for i in range(len(selections)):
        selected_cards.append(cards[i][selections[i] - 1])
    possible = [x for x in selected_cards[0] if x in selected_cards[1]]
    if len(possible)==0:
        return "Volunteer cheated!"
    elif len(possible)==1:
        return possible[0]
    else:
        return "Bad magician!"

def main():
    with open('input.in', 'r') as f:
        with open('output.txt', 'w') as o:
            n = int(f.readline().rstrip('\n'))
            for i in range(n):
                cards = []
                selections = []
                for j in range(2):
                    selections.append(int(f.readline().rstrip('\n')))
                    current_cards = []
                    for k in range(4):
                        current_cards.append(f.readline().rstrip('\n').split(' '))
                    cards.append(current_cards)
                result = "Case #" + str(i + 1) + ": " + magic_trick(cards, selections)
                print(result)
                o.write(result + "\n")

if __name__=="__main__":
    main()
