#! /usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', 
                    action='store_true',
                    default=False,
                    dest='largeFile',
                    help='Use large practice input instead of small one.')

def isWinner(array, player):
    length = len(array)
    for row in array:
        letters = ''.join(row)
        if test(letters, player):
            return True

    for index in xrange(length):
        letters = ''.join([row[index] for row in array])
        if test(letters, player):
            return True

    # Diagonals
    uprightIndex, upleftIndex = (0, length-1)
    inARow = 4
    for iterations in xrange(length+1-inARow):
        leftString, rightString = ('', '')
        leftIndex, rightIndex = (upleftIndex, uprightIndex)
        for row in range(length-1, -1, -1):
            if leftIndex >= 0:         leftString += array[row][leftIndex]
            if rightIndex <= length-1: rightString += array[row][rightIndex]
            leftIndex -= 1
            rightIndex += 1
        if test(leftString, player) or test(rightString, player):
            return True
        upleftIndex -= 1
        uprightIndex += 1

    for row in range(length-2, inARow-2, -1):
        upleftIndex, uprightIndex = (length-1, 0)
        leftString, rightString = ('', '')
        for diagonalRow in range(row, -1, -1):
            if upleftIndex >= 0: leftString += array[diagonalRow][upleftIndex]
            if uprightIndex <= length-1: rightString += array[diagonalRow][uprightIndex]
            upleftIndex -= 1
            uprightIndex += 1
        if test(leftString, player) or test(rightString, player):
            return True

    return False

def noEmptyCells(data):
    for row in data:
        if '.' in row:
            return False 
    return True

def result(data):
    player1 = isWinner(data, 'X')
    player2 = isWinner(data, 'O')
    if player1 and not player2:
        return 'X won'
    if not player1 and player2:
        return 'O won'
    if not player1 and not player2 and noEmptyCells(data):
        return 'Draw'
    else:
        return 'Game has not completed'


def test(string, letter):
    if '.' in string:
        return False
    for char in string:
        if char != letter and char != 'T':
            return False
    return True

if __name__ == '__main__':
    args = vars(parser.parse_args())
    filename = 'A-small-attempt0.in' if not args['largeFile'] else 'A-large.in'
    try:
        contents = open(filename).read().splitlines()
    except:
        raise

    totalCases = int(contents[0])
    row = 1
    testData = [['.' for x in xrange(4)] for y in xrange(4)]
    for case in xrange (1, totalCases+1):
        for testDataRow in xrange(4):
            for testDataCol in xrange(4):
                testData[testDataRow][testDataCol] = contents[row][testDataCol]
            row += 1
        row += 1

        print 'Case #'+ str(case) + ': ' + result(testData)
