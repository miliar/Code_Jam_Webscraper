import os
import sys

class funny_jam:
    IN =sys.stdin;
    case_num =0;
    result ={'XO': 'Draw',
             'X': 'X won',
             'O': 'O won',
             'N/A':'Game has not completed'}
    search_path =[
        #diagonal 
        [[0, 0], [1, 1], [2, 2], [3, 3]],
        [[0, 3], [1, 2], [2, 1], [3, 0]],
        #horizontal
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[1, 0], [1, 1], [1, 2], [1, 3]],
        [[2, 0], [2, 1], [2, 2], [2, 3]],
        [[3, 0], [3, 1], [3, 2], [3, 3]],
        #vertical
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 1], [1, 1], [2, 1], [3, 1]],
        [[0, 2], [1, 2], [2, 2], [3, 2]],
        [[0, 3], [1, 3], [2, 3], [3, 3]],];
    winner ='';
    
    @classmethod
    def cases(klz):
        return int(klz.IN.readline());

    @classmethod
    def line(klz):
        return klz.IN.readline().strip();
    
    @classmethod
    def out_a_line(klz):
        klz.case_num +=1;
        print "Case #%d: %s" % (klz.case_num, klz.result.get(klz.winner, 'error!!!!'));
        klz.winner ='';

    @classmethod
    def find_winner(klz, symbol, mat):
        klz.winner +=symbol;
        for path in klz.search_path:
            ct =0;
            for [x, y] in path:
##                sys.stderr.write("\ncurr: %s, (x,y):(%d, %d)" % (mat[x][y][0], x, y));
                if 'T' ==mat[x][y][0]:
                    ct +=1;
                    continue;
                if symbol ==mat[x][y][0]:
                    ct +=1;
                    continue;
            if 4 ==ct:
                return symbol;

        return '';            

    @classmethod
    def is_complete(klz, mat):
        if '' ==klz.winner:
            for row in mat:
                if ['.'] in row:
                    return 'N/A';
            return 'XO';
        return '';
        
        
    @classmethod
    def solve(klz, mat):
        for symbol in ["X", "O"]:
            klz.winner +=klz.find_winner(symbol, mat);
        klz.winner += klz.is_complete(mat);
        klz.out_a_line();
        
def go():
    cases =funny_jam.cases();
    for ct in xrange(cases):
        mat =[];
        for board in xrange(4):
            mat.append([[row] for row in funny_jam.line()]);
        funny_jam.solve(mat);
        funny_jam.line();



if __name__ == '__main__':
    stdin =sys.stdin;
    stdout =sys.stdout;
    sys.stdin =open("test.in", "r")
    sys.stdout =open("test.out", "w");
    go();
    sys.stdin.close();
    sys.stdin.close();
    sys.stdin =stdin;
    sys.stdout =stdout;


