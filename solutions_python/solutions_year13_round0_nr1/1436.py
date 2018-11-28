import sys
from multiprocessing import Pool

def calc(line, data = None):
    if data is None:
        data = {'X':0, 'O':0, 'T':0, '.':0}
    
    for c in line:
        if c in data:
            data[c] += 1
        else:
            print >> sys.stderr, "Unkown c %s" % c
    return data

def main(game):
    dataset = (game, zip(*game), \
               ((game[0][0], game[1][1], game[2][2], game[3][3]), \
                (game[0][3], game[1][2], game[2][1], game[3][0])))
    for ds in dataset:
        for line in ds:
            d = calc(line)
            if d['X'] + d['T'] == 4:
                return 'X won'
            elif d['O'] + d['T'] == 4:
                return 'O won'
            
    data = None
    for row in game:
        data = calc(row, data)
    if data['X'] + data['O'] + data['T'] == 16:
        return 'Draw'
    else:
        return 'Game has not completed' 
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = open("test.txt")
    T = int(f.readline())
    data = list()
    
    for i in range(T):
        game = list()
        for j in range(4):
            row = tuple(f.readline().strip())
            game.append(row)
        f.readline()
        data.append(game)
        
    pool = Pool()
    result = pool.map(main, data)
#    result = map(main, data)
    for i in range(T):
        print "Case #%d: %s" % (i+1, result[i])
        