import sys

class Trick:
    def __init__(self):
        self.has_multiple = False
        self.has_solution = False
        self.row1 = []
        self.row2 = []
        self.solution = 0

def get_row(fin, row_num):
    for i in range(4):
        temp = fin.readline()
        if i == row_num:
            row = temp.split(' ')
    for i in range (len(row)):
        row[i] = int(row[i])
    row.sort()
    return row


def read_input(fin, num_games):
    tricks = []
    for i in range(num_games):
        temp = Trick()
        row_num = int(fin.readline()) -1
        temp.row1 = get_row(fin, row_num)
        row_num = int(fin.readline()) -1
        temp.row2 = get_row(fin, row_num)
        tricks.append(temp)
    return tricks

def evaluate_tricks(tricks, num_games):
    for i in range(num_games):
        for j in range(len(tricks[i].row1)):
            for k in range(len(tricks[i].row2)):
                if tricks[i].row1[j] == tricks[i].row2[k]:
                    if tricks[i].has_solution == True:
                        tricks[i].has_multiple = True
                        break
                    else:
                        tricks[i].has_solution = True
                        tricks[i].solution = tricks[i].row1[j]
    return tricks

def print_tricks(tricks, num_games):
    for i in range (num_games):
        if tricks[i].has_multiple == True:
            print ("Case #{}: Bad magician!".format(i+1))
        elif tricks[i].has_solution == True:
            print ("Case #{}: {}".format((i+1), tricks[i].solution))
        else:
            print ("Case #{}: Volunteer cheated!".format(i+1))

def main():
    input_name = sys.argv[1]
    fin = open(input_name, 'r')

    num_games = int (fin.readline())
    tricks = read_input(fin, num_games)
    tricks = evaluate_tricks(tricks, num_games)
    print_tricks(tricks, num_games)


if __name__ == '__main__':
    main()
