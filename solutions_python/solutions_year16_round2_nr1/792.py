from sys import stdin


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def deleted(letters, character, times):
    count = letters.count(character)
    return list(filter(character.__ne__, letters)) + [character] * (times - count)


def solve_case():
    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    all_letters = set(''.join(digits))
    counts = {}
    for letter in all_letters:
        counts[letter] = 0
    
    letters = list(read_str())

    for letter in letters:
        counts[letter] += 1
    
    zeros = counts['Z']
    counts['Z'] -= zeros
    counts['E'] -= zeros
    counts['R'] -= zeros
    counts['O'] -= zeros
    
    twos = counts['W']
    counts['T'] -= twos
    counts['W'] -= twos
    counts['O'] -= twos
    
    fours = counts['U']
    counts['F'] -= fours
    counts['O'] -= fours
    counts['U'] -= fours
    counts['R'] -= fours
    
    sixs = counts['X']
    counts['S'] -= sixs
    counts['I'] -= sixs
    counts['X'] -= sixs
    
    sevens = counts['S']
    counts['S'] -= sevens
    counts['E'] -= 2 * sevens
    counts['V'] -= sevens
    counts['N'] -= sevens
    
    eights = counts['G']
    counts['E'] -= eights
    counts['I'] -= eights
    counts['G'] -= eights
    counts['H'] -= eights
    counts['T'] -= eights
    
    fives = counts['V']
    counts['F'] -= fives
    counts['I'] -= fives
    counts['V'] -= fives
    counts['E'] -= fives

    threes = counts['R']
    
    ones = counts['O']
    
    nines = counts['I']
    
    return zeros * '0' + ones * '1' + twos * '2' + threes * '3' + fours * '4' + fives * '5' + sixs * '6' + sevens * '7' + eights * '8' + nines * '9'
    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {}'.format(case, solve_case()))

        
if __name__ == '__main__':
    main()
