import sys

def main():
    inp = open(sys.argv[1])
    print(magician(inp))

def magician(input):
    input = input.read().splitlines()
    result = ''
    for i in range(1,int(input[0])+1):
        chosen_index = 10*i-9
        row = int(input[chosen_index])
        first_nums = input[chosen_index+row].split()
        
        chosen_index = 10*i-4
        row = int(input[chosen_index])
        second_nums = input[chosen_index+row].split()
        
        answer = list(set(first_nums) & set(second_nums))
        if len(answer) == 1:
            result += 'Case #{}: {}\n'.format(i, answer[0])
        elif len(answer) == 0:
            result += 'Case #{}: Volunteer cheated!\n'.format(i)
        elif len(answer) > 1:
            result += 'Case #{}: Bad magician!\n'.format(i)
    return result

if __name__ == '__main__':
    main()
