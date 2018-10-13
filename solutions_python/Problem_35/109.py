# Marius Damarackas (m.damarackas@gmail.com)
# Google CodeJam, Qualification Round 2009, Watersheds

import itertools

infty = 123456789
cur_label = "a"
delta = ((-1, 0), (0, -1), (0, 1), (1, 0))

def is_sink(altitudes, row, col):
    height, width = len(altitudes), len(altitudes[0])
    neighbours = [altitudes[row + dr][col + dc] for dr, dc in delta
                  if 0 <= row + dr < height and 0 <= col + dc < width]
    return len(neighbours) == 0 or altitudes[row][col] <= min(neighbours)

def create_label(altitudes, labels, row, col):
    height, width = len(altitudes), len(altitudes[0])
    if labels[row][col] is not None:
        return labels[row][col]
    elif is_sink(altitudes, row, col):
        global cur_label
        labels[row][col] = cur_label
        cur_label = chr(ord(cur_label) + 1)
        return labels[row][col]
    else:
        next_row, next_col, min_alt = infty, infty, infty
        for dr, dc in delta:
            if 0 <= row + dr < height and 0 <= col + dc < width:
                tr, tc = row + dr, col + dc
                if altitudes[tr][tc] < min_alt:
                    next_row, next_col, min_alt = tr, tc, altitudes[tr][tc]            
        labels[row][col] = create_label(altitudes, labels, next_row, next_col)
        return labels[row][col]      

def label_map(altitudes):
    global cur_label
    cur_label = "a"
    height, width = len(altitudes), len(altitudes[0])
    labels = [[None for i in range(width)] for j in range(height)]
    for row, col in itertools.product(range(height), range(width)):
        create_label(altitudes, labels, row, col)
    return labels
                
def main():
    file = open("input.in")
    tests = int(file.readline())
    for case in range(1, tests + 1):
        height, width = [int(x) for x in file.readline().split()]
        altitudes = []
        for i in range(height):
            altitudes.append([int(x) for x in file.readline().split()])
        print("Case #", case, ":", sep="")
        labels = label_map(altitudes)
        for i in range(height):
            print(" ".join([str(x) for x in labels[i]]))

if __name__ == "__main__":
    main()
