import math



def cost(column, width):
    column -= (width - 1)
    if column % width > 0:
        return column // width + 1
    else:
        return column // width


def main():
    fin = open('input.in', 'r')
    fout = open('output.txt' , 'w')
    file = fin.read().split('\n')
    file.pop(0)
    file.pop()

    for count, line in enumerate(file):
        rows, columns, width = [int(x) for x in line.split()]
        turns = cost(columns, width) * rows
        if columns % width == 0:
            turns += width - 1
        else:
            turns += width
        fout.write("Case #{0}: {1}\n".format(count + 1, turns))

    
    fout.close()
    fin.close()

if __name__ == "__main__":
    main()
