import sys

def flip(string, k):
    flipped = 0
    string = list(string)
    while "-" in string:
        if k == len(string) and '+' in string:
            return "IMPOSSIBLE"
        print("".join(string))
        for i in range(len(string)):
            if string[i] == '-':
                if i + k > len(string):
                    return "IMPOSSIBLE"
                for j in range(i, i + k):
                    string[j] = '+' if string[j] == '-' else '-'
                flipped += 1
                break
    return flipped

def parser(filename):
    with open(filename.replace('in','out'), 'w') as o:
        with open(filename) as f:
            cases = int(f.readline())
            print("{} cases".format(cases))

            for i in range(cases):
                n = f.readline().replace('\n','')
                string, k = n.split(' ')
                o.write('Case #{}: {}\n'.format(i+1, flip(string, int(k))))


if __name__ == '__main__':
    #print(flip('-++++++++-',9))
    parser(sys.argv[1])
        
