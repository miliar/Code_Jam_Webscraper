import sys

def main():
    for i,line in enumerate(sys.stdin):
        if i != 0:
            line = line.strip().split(' ')
            s = line[1]
            total,extra = 0,0
            for index, c in enumerate(s):
                if int(c) != 0 and index > total:
                    extra += index - total
                    total += extra
                total += int(c)
            print('Case #' + str(i) + ': ' + str(extra))

if __name__ == '__main__':
    main()
