inputs = open("input.txt", "r").read().split("\n")[1:]
output = open("output.txt", "w")
grids = []
finished_grids = []

def only(string, char):
    for a in range(len(string)):
        if string[a] != char:
            return False
    return True

while len(inputs) > 0:
    grid_size = [int(x) for x in inputs[0].split(" ")]
    grid = []

    for a in range(grid_size[0]):
        grid.append(inputs[a + 1])

    inputs = inputs[grid_size[0] + 1:]
    grids.append(grid)

for a in range(len(grids)):
    temp_grid = grids[a]
    finished_grid = []

    while "?" in "".join(temp_grid):
        for b in range(len(temp_grid)):
            string = temp_grid[b]

            for c in range(len(string)):
                if only(string, "?"):
                    if b == 0:
                        first_has_letter = 0
                        temp = temp_grid[first_has_letter]

                        while only(temp, "?"):
                            first_has_letter += 1
                            temp = temp_grid[first_has_letter]

                        for d in range(first_has_letter):
                            temp_grid[d] = temp_grid[first_has_letter]

                        string = temp_grid[first_has_letter]
                    else:
                        first_has_letter = b
                        temp = temp_grid[first_has_letter]

                        while only(temp, "?"):
                            first_has_letter -= 1
                            temp = temp_grid[first_has_letter]

                        for d in range(b, first_has_letter, -1):
                            temp_grid[d] = temp_grid[first_has_letter]

                        string = temp_grid[first_has_letter]

                elif string[c] == "?" and c == 0:
                    first_letter = 0
                    temp = string[first_letter]

                    while temp == "?":
                        first_letter += 1
                        temp = string[first_letter]

                    string = string[first_letter] * first_letter + string[first_letter:]

                elif string[c] == "?":
                    string = string[:c] + string[c - 1] + string[c + 1:]

            temp_grid[b] = string

    finished_grids.append(temp_grid)

output.write("\n".join(["Case #" + str(x + 1) + ":\n" + "\n".join(finished_grids[x]) for x in range(len(finished_grids))]))
