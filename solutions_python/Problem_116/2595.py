#!/bin/env python

import sys, string, numpy

class Board:
  def __init__(self, text):
    self.__data = numpy.empty((4, 4), dtype = 'uint8')
    for rowIndex, line in enumerate(text):
      translationTable = string.maketrans('XOT.', '0123')
      translatedLine = line.translate(translationTable)
      lineAsFloatRow = map(lambda x: int(x), translatedLine)
      self.__data[rowIndex, :] = lineAsFloatRow 

  def array_str(self):
    return numpy.array_str(self.__data)

  def __str__(self):
    return str(self.__data)

  def __repr__(self):
    return repr(self.__data)

  def status(self):
    xWinSlc = set([0, 2])
    oWinSlc = set([1, 2])

    for slc in self.__data:
      if set(slc) <= xWinSlc:
        return 'X won'
      if set(slc) <= oWinSlc:
        return 'O won'

    for slc in self.__data.T:
      if set(slc) <= xWinSlc:
        return 'X won'
      if set(slc) <= oWinSlc:
        return 'O won'

    diagSet = set(self.__data.diagonal()) 
    if diagSet <= xWinSlc:
      return 'X won'
    if diagSet <= oWinSlc:
      return 'O won'

    antidiagSet = set(numpy.fliplr(self.__data).diagonal())
    if antidiagSet <= xWinSlc:
      return 'X won'
    if antidiagSet <= oWinSlc:
      return 'O won'

    if numpy.any(self.__data == 3):
      return 'Game has not completed'
    else:
      return 'Draw'

if __name__ == '__main__':
  with open(sys.argv[1]) as infile, open('results.txt', 'w') as outfile:
    numberOfBoards = int(infile.readline())
    for boardNumber in range(numberOfBoards):
      boardText = [infile.readline().rstrip() for _ in range(4)]
      infile.readline() # throw away blank line
      board = Board(boardText)
      outfile.write('Case #' + str(boardNumber + 1) + ': ' + board.status() + '\n')

