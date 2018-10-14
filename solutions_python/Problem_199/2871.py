import fileinput

def flip_pancake(pancake):
    if pancake == '-':
        return '+'
    else:
        return '-'

def main():
    have_read_first_line = False
    case = 1
    
    for line in fileinput.input():
        if not have_read_first_line:
            have_read_first_line = True
            continue
        
        pancakes, flipsize = line.split()
        flipsize = int(flipsize)
        pancakes = list(pancakes)
        
        flips = 0
        for index in range(len(pancakes)-flipsize+1):
            # Pancakes must be flipped
            if pancakes[index] == '-':
                flips += 1
                for flip_index in range(flipsize):
                    pancake = pancakes[index + flip_index]
                    pancakes[index + flip_index] = flip_pancake(pancake)
        
        succeeded = True
        for index in range(len(pancakes)):
            if pancakes[index] != '+':
                succeeded = False
                break
        
        print('Case #' + str(case) + ': ' +
              (str(flips) if succeeded else 'IMPOSSIBLE'))
        case += 1

if __name__ == '__main__':
    main()