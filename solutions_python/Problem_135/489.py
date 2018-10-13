def process_input(rows):
    return [[int(card) for card in row.split(" ")] for row in rows]

def main():
    with open('A.in') as f:
        with open('A.out', 'w') as f2:
            text = f.readlines()
            for i in range(int(text[0])):
                answer1, answer2 = int(text[1 + 10*i]), int(text[6 + 10*i])
                cards1, cards2 = process_input(text[2 + 10*i:6 + 10*i]), process_input(text[7 + 10*i:11 + 10*i])
                possible1 = cards1[answer1-1]
                possible2 = cards2[answer2-1]
                possible = [card for card in possible1 if card in possible2]
                output = "Case #" + str(i+1) + ": "
                if len(possible) == 1:
                    output += str(possible[0])
                elif len(possible) > 1:
                    output += "Bad magician!"
                else:
                    output += "Volunteer cheated!"
                print(output)
                f2.write(output + "\n")

main()