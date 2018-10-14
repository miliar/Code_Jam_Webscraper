def min_years(alien_sym):
    unique_sym = []
    for i in alien_sym:
        if (i not in unique_sym):
            unique_sym.append(i)

    base = len(unique_sym)
    if(base == 1):
        base = 2
    

##    print(unique_sym)
    num = 0
    i = len(alien_sym)-1
    for x in alien_sym:
        digit = unique_sym.index(x)
        if (digit == 0):
            digit = 1
        elif (digit == 1):
            digit = 0

        num = num + (digit)*pow(base, i)
        i = i - 1
    print(num)

def main():
    with open(r'D:\Documents\CodeJam\2009\round1C\A-large.in', 'r') as f:
        n = int(f.readline())
        for i in range(0, n):
            line = f.readline()[:-1]
            print("Case #{0:d}: ".format(i+1), end='')
            min_years(line)
            

if __name__=='__main__':
    main()
