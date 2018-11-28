import sys
def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        row_first = []
        row_second = []
        row_first_num = int(sys.stdin.readline())
        for j in range(4):
            if j == row_first_num-1:
                row_first = map(int, sys.stdin.readline().split())
            else:
                temp = map(int, sys.stdin.readline().split())
        row_second_num = int(sys.stdin.readline())
        for j in range(4):
            if j == row_second_num-1:
                row_second = map(int, sys.stdin.readline().split())
            else:
                temp = map(int, sys.stdin.readline().split())
        result = list(set(row_first) & set(row_second))
        if len(result) == 1:
            print "Case #" + str(i+1) + ": " + str(result[0])
        elif len(result) > 1:
            print "Case #"+ str(i+1) + ": Bad magician!"
        else:
            print "Case #"+ str(i+1) + ": Volunteer cheated!"
        
                
        
if __name__ == "__main__":
	main();
