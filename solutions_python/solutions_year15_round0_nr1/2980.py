def main():
    n = int(input())
    for x in range(1, n+1):
        line = input().split()
        standing = 0
        required = 0
        for i in range(int(line[0])+1):
            shyness = i
            nopwtl = int(line[1][shyness])
            if standing >= shyness:
                standing += nopwtl
            else:
                while standing < shyness:
                    standing += 1
                    required += 1
                standing += nopwtl
        if standing == 0:
        	required += 1
        print("Case #%d:"%x, required)
    return 0
if __name__ == '__main__':
    main()
