def find_game_state(array):
    not_completed_possible = False

    for line in array:

        player = ""

        for i, letter in enumerate(line):
            print "linea ", line
            if letter == ".":
                not_completed_possible = True
                break

            if letter == "T":
                if player:
                    if i == 3:
                        return player + " won"
                    else:
                        continue
                else:
                    player = letter

            else:
                if not player:
                    player = letter
                    continue
                if player == letter:
                    if i == 3:
                        return player + " won"
                    continue
                if player == "T":
                    player = letter
                else:
                    break

    if not_completed_possible:
        return "Game has not completed"
    else:
        return "Draw"

def main():
    with open("output.txt", "w") as output:
        with open("input.txt", "r") as f:
            number = int(f.readline())
            i = 0
            print number
            while i < number:
                print i
                j = 0
                array = []
                while j < 4:
                    array.append(f.readline())
                    j += 1
                # Consume empty line
                f.readline()
                
                # Add verticals
                v1 = ""
                v2 = ""
                v3 = ""
                v4 = ""

                # Add diagonals
                diagonal1 = ""
                diagonal2 = ""

                for index, line in enumerate(array):
                    print "line ", line
                    v1 += line[0]
                    v2 += line[1]
                    v3 += line[2]
                    v4 += line[3]
                    diagonal1 += line[index]
                    index2 = 3 - index
                    diagonal2 += line[index2]
                
                for element in [v1, v2, v3, v4, diagonal1, diagonal2]:
                    array.append(element)
                    print "element", element
                num = str(i + 1)
                output.write("Case #" + num + ": ")
                output.write(find_game_state(array))
                output.write("\n")
                i += 1

main()
