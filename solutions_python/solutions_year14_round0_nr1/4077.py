#!/usr/bin/python

import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        num_inputs = int(f.readline())
        for i in xrange(0, num_inputs):
            first_answer = int(f.readline())
            first_arrangement = []
            for j in xrange(0, 4):
                row = f.readline().strip().split(" ")
                for card in row:
                    first_arrangement.append(card)
            # print first_arrangement
            second_answer = int(f.readline())
            second_arrangement = []
            for j in xrange(0, 4):
                row = f.readline().strip().split(" ")
                for card in row:
                    second_arrangement.append(card)
            # print second_arrangement
            
            first_row = first_arrangement[(first_answer-1)*4:(first_answer-1)*4+4]
            # print first_row
            second_row = second_arrangement[(second_answer-1)*4:(second_answer-1)*4+4]
            # print second_row

            counter = 0
            card = ''
            for item in first_row:
                if item in second_row:
                    counter = counter + 1
                    card = item

            title = 'Case #%d: %s'
            if counter == 0:
                print title % (i+1, 'Volunteer cheated!')
            if counter == 1:
                print title % (i+1, card)
            if counter > 1:
                print title % (i+1, 'Bad magician!')

