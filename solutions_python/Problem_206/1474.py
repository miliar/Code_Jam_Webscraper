import sys

def main():
    total = int(sys.stdin.readline())
    for i in range(total):
        line = sys.stdin.readline()
        d, n = map(lambda x: int(x), line.rstrip().split(' '))

        max_time = 0
        for j in range(n):
            line = sys.stdin.readline()
            k, s = map(lambda x: int(x), line.rstrip().split(' '))
            max_time = max((d-k)/s, max_time)
            
        max_speed = d / max_time
        print ('Case #{}: {}'.format(i + 1, max_speed))
    
if __name__ == "__main__":
    main()