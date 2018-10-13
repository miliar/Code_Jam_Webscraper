from sys import argv

def standing_ovation_num(digits):
    extras = 0
    count = 0
    
    for i, d in enumerate(digits):
        count += d
        while(count <= i):
            count += 1
            extras += 1
    
    return extras


if __name__ == '__main__':
    filename = argv[1]

    with open(filename, "r") as f:
        f.readline()
        
        for i, line in enumerate(f):
            s_max, digits = line.rsplit()
            digits = map(int, list(digits))
            extras = standing_ovation_num(digits)
            print("Case #{}: {}".format(i+1, extras))