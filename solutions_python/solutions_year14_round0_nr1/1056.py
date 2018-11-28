#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    in_file = open("A-small-attempt0.in", mode='r')
    out_file = open("A-small-attempt0.out", mode='w')

    T = int(in_file.readline())
    
    for i in range(T):
        choice1, cards1 = readCards(in_file)
        choice2, cards2 = readCards(in_file)
        row1 = set(cards1[choice1-1])
        row2 = set(cards2[choice2-1])
        answer = row1 & row2

        if len(answer) == 0:
            out_file.write("Case #" + str(i+1) + ": Volunteer cheated!" + "\n") 
        elif len(answer) == 1:
            out_file.write("Case #" + str(i+1) + ": " + str(list(answer)[0]) + "\n") 
        else:
            out_file.write("Case #" + str(i+1) + ": Bad magician!" + "\n") 

    in_file.close()
    out_file.close()

def readCards(in_file):
    choice = int(in_file.readline())
    cards = [[int(x) for x in in_file.readline().strip().split()] for i in range(4)]
    return (choice, cards)


if __name__ == '__main__':
    main()