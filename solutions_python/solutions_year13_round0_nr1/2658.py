#gsoc qualiA

# 0: vacio
# 1: X
# 2: O
# 3: T

def test(array):
    combinaciones = (((0,0),(0,1),(0,2),(0,3)),
                     ((1,0),(1,1),(1,2),(1,3)),
                     ((2,0),(2,1),(2,2),(2,3)),
                     ((3,0),(3,1),(3,2),(3,3)),
                     
                     ((0,0),(1,0),(2,0),(3,0)),
                     ((0,1),(1,1),(2,1),(3,1)),
                     ((0,2),(1,2),(2,2),(3,2)),
                     ((0,3),(1,3),(2,3),(3,3)),

                     ((0,0),(1,1),(2,2),(3,3)),
                     ((0,3),(2,1),(1,2),(3,0)))

    for comb in combinaciones:
        fila = tuple()
        for x,y in comb:
            fila += (array[x][y],)

        X = fila.count(1)
        O = fila.count(2)
        T = fila.count(3)
        if X + T == 4:
            print("X won")
            return
        elif O + T == 4:
            print("O won")
            return

    draw = True
    for fila in array:
        if 0 in fila:
            draw = False
            break
    if draw == True:
        print("Draw")
        return

    print("Game has not completed")

# ----
def main():
    for i in range(int(input())):
        array = []

        for j in range(4):
            array += [ list( map(int, input().replace('.', '0')
                                             .replace('X', '1')
                                             .replace('O', '2')
                                             .replace('T', '3'))) ]
        input()
        print("Case #%s: " % str(i+1), end = '')
        test(array)

if __name__ == '__main__': main()
