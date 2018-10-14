import ttt

def main():
        #filename = "test.txt"
        #filename = "A-small-attempt0.in"
        filename = "A-large.in"
        with open(filename, 'r') as f:
                num_cases = int(f.readline())
                for i in range(0, num_cases):
                        grid = []
                        for j in range(0, 4):
                                grid.append(list(f.readline())[0:4])
                        state = ttt.BoardState(grid)
                        print "Case #%d: %s" % (i+1, ttt.validate_board(state))
                        f.readline()

if  __name__ == '__main__':
        main()
