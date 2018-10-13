import linecache

class Square:
    def __init__(self, mm):
        self.mm = mm
        self.state = 'N'

def show_lawn(lawn):
    for row in lawn:
        print('[', end=' ')
        for square in row:
            print('({}, {})'.format(square.mm, square.state), end=' ')
        print(']')


cases = 100
txtlines = 1323
filename = 'large.in'

case = 1
txtline = 1
while case <= cases and txtline <= txtlines:
    rectangle = linecache.getline(filename, txtline).split()
    N, M = int(rectangle[0]), int(rectangle[1])
    
    horizontal_lawn = []
    for i in range(1, N+1):
        row = linecache.getline(filename, txtline+i).split()
        tmprow = []
        for value in row:
            tmprow.append(Square(int(value)))
        horizontal_lawn.append(tmprow)
    
    vertical_lawn = [[row[i] for row in horizontal_lawn] for i in range(len(horizontal_lawn[0]))]

    for row in horizontal_lawn:
        max = 0
        for square in row:
            if max < square.mm:
                max = square.mm
        # cut
        for square in row:
            if max == square.mm:
                square.state = 'Y'
    
    #show_lawn(horizontal_lawn)
    #print()
    #show_lawn(vertical_lawn)
    
    for row in vertical_lawn:
        ok = True
        for square in row:
            if square.state == 'N':
                ok = False
        if not ok:
            max = 0
            for square in row:
                if max < square.mm:
                    max = square.mm
            # cut
            for square in row:
                if max == square.mm:
                    square.state = 'Y'
    
    #print()
    #show_lawn(vertical_lawn)
    
    # Take result
    result = 'YES'
    for row in vertical_lawn:
        for square in row:
            if square.state == 'N':
                result = 'NO'
    
    print('Case #{}: {}'.format(case, result))
    case = case + 1
    txtline = txtline + N + 1

#horizontal_lawn = [
#        [Square(2), Square(1), Square(2)],
#        [Square(1), Square(1), Square(1)],
#        [Square(2), Square(1), Square(2)]
#    ]
#horizontal_lawn = [
#        [Square(2), Square(2), Square(2), Square(2), Square(2)],
#        [Square(2), Square(1), Square(1), Square(1), Square(2)],
#        [Square(2), Square(1), Square(2), Square(1), Square(2)],
#        [Square(2), Square(1), Square(1), Square(1), Square(2)],
#        [Square(2), Square(2), Square(2), Square(2), Square(2)]
#    ]
#horizontal_lawn = [
#        [Square(1), Square(2), Square(1)]
#    ]