import sys

def tidy(string):
    n = list(string)
    length = len(n)
    if length == 1:
        return int(''.join(n))
    for i in range(0, length-1):
        if n[i] > n[i+1]: #there exists a non tidy seq
            n[-1] = '-1'
            for j in range(1, length):
                if n[-j-1] > n[-j] or i < (length - j): #if a>b
                    n[-j-1] = str(int(n[-j-1])-1)
                    n[-j] = '9'                    
    return int(''.join(n))

def main():
    with open(sys.argv[1], 'r') as infile:
        for i, line in enumerate(infile):
            if i == 0:
                continue
            print("Case #" + str(i) + ": " + str(tidy(line.strip())) )

if __name__ == "__main__":
    main()