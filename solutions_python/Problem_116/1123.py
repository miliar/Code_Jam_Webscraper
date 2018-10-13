import sys;
import math;
import operator;
import collections;

class _:
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return ""
    pass

if __name__ == "__main__":
    n_cases = int(sys.stdin.readline())

    for _i in range(n_cases):
        # Reading...
        result = 0
        lines = []
        lines.append( sys.stdin.readline()[:-1]);
        lines.append( sys.stdin.readline()[:-1]);
        lines.append( sys.stdin.readline()[:-1]);
        lines.append( sys.stdin.readline()[:-1]);
        sys.stdin.readline();

        # Solving...
        cases = list(lines)
        cases.append( ''.join( [ x[0] for x in lines ] ) )
        cases.append( ''.join( [ x[1] for x in lines ] ) )
        cases.append( ''.join( [ x[2] for x in lines ] ) )
        cases.append( ''.join( [ x[3] for x in lines ] ) )
        cases.append( lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3] )
        cases.append( lines[3][0] + lines[2][1] + lines[1][2] + lines[0][3] )

        gameIsCompleted = True

        for _line in lines:
            for j in _line:
                if j == '.':
                    gameIsCompleted = False

        for case in cases:
            winner = 'T'
            thereIsWinner = True

            for move in case:
                # print "comparando %s, %s %s"%(winner, case, move)
                if move == '.':
                    thereIsWinner = False
                    break

                if move == 'T':
                    continue

                if winner == 'T':
                    winner = move
                else:
                    if move != winner:
                        thereIsWinner = False
                        break

            # print "Encontramos un ganador: %s %s "%(thereIsWinner, gameIsCompleted)

            if thereIsWinner:
                result = winner + " won"
                break
            else:
                if gameIsCompleted:
                    result = "Draw"
                else:
                    result = "Game has not completed"

        # printing...
        #sys.stderr.write("Case #%s: %s Done!\n"%(_i+1, result))
        print "Case #%s: %s"%(_i+1, result)

