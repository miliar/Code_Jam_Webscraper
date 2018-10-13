#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Board:
    def __init__(self, data):
        self.data = data
        self.lines = {'cols': [{'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}],
                      'rows': [{'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}],
                      'diags': [{'prev': '.', 'cnt': 0}, {'prev': '.', 'cnt': 0}]
                      }
        self.diag = ((0, 3), (1, 2), (2, 1), (3, 0))
        self.is_full = True

    def get_result(self):
        col_num = 0
        row_num = 0
        for line in self.data:
            for cell in line:
                self.calc(row_num, col_num, cell);
                col_num += 1
                if col_num is 4:
                    col_num = 0
                    break
                
            row_num += 1
        #print self.lines

        for result in (self.lines['cols'] + self.lines['rows'] + self.lines['diags']):
            if result['cnt'] == 4:
                return result['player'] + ' won'

        if self.is_full:
            return 'Draw'
        else:
            return 'Game has not completed'

    def calc(self, row_num, col_num, cell):
        prev_col_cell = self.lines['cols'][col_num]['prev']
        self.lines['cols'][col_num]['prev'] = cell
        prev_row_cell = self.lines['rows'][row_num]['prev']
        self.lines['rows'][row_num]['prev'] = cell
        if cell == 'X' or cell == 'O':
            self.lines['cols'][col_num]['player'] = cell
            self.lines['rows'][row_num]['player'] = cell
        
        #print str(row_num) + ':' + str(col_num) + ', ' + self.lines['rows'][row_num]['prev']

        diag_num = self.get_diag_num(col_num, row_num)
        if diag_num is not -1:
            prev_diag_cell = self.lines['diags'][diag_num]['prev']
            self.lines['diags'][diag_num]['prev'] = cell
            if cell == 'X' or cell == 'O':
                self.lines['diags'][diag_num]['player'] = cell
        
        if cell == '.':
            self.is_full = False
            self.lines['cols'][col_num]['cnt'] = 0
            self.lines['rows'][row_num]['cnt'] = 0
            if diag_num is not -1:
                self.lines['diags'][diag_num]['cnt'] = 0
            return

        if cell == 'T' or prev_col_cell == 'T' or cell == prev_col_cell:
            self.lines['cols'][col_num]['cnt'] += 1
        else:
            self.lines['cols'][col_num]['cnt'] = 1
            

        if cell == 'T' or prev_row_cell == 'T' or cell == prev_row_cell:
            self.lines['rows'][row_num]['cnt'] += 1
        else:
            self.lines['rows'][row_num]['cnt'] = 1

        if diag_num != -1:
            if cell == 'T' or prev_diag_cell == 'T' or cell == prev_diag_cell:
                self.lines['diags'][diag_num]['cnt'] += 1
            else:
                self.lines['diags'][diag_num]['cnt'] = 1


    def get_diag_num(self, col_num, row_num):
        if col_num is row_num:
            return 0
        if (col_num, row_num) in self.diag:
            return 1
        return -1
        

def solve():
    line_cnt = -1
    test_num = 0
    data = []
    case_num = 1
    for line in open('A-small-attempt0.in', 'r'):
        line_cnt += 1
        if line_cnt is 0:
            test_num = int(line)
            continue

        row = line.rstrip()
        if row is '':
            continue

        data.append(row)
        if len(data) is 4:
            board = Board(data);
            data = []
            print 'Case #' + str(case_num) + ': ' + board.get_result()
            case_num += 1

if __name__ == '__main__':
    solve()
