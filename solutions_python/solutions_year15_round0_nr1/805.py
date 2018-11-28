import sys

def readline(line):
    str_s = line.strip('\n').split(' ')[1]
    print list(str_s)
    return [int(d) for d in str_s]

def ovation(S):
    guests_standing = 0
    friends_needed = 0
    total_standing = 0
    for level, guests in enumerate(S):
        friends_needed += max(0, level - total_standing)
        guests_standing += guests
        total_standing = guests_standing + friends_needed
    return friends_needed



def main(file_in, file_out):
    results = []
    with open(file_in, 'r') as fin:
        T = next(fin)
        for line in fin:
            S = readline(line)
            result = ovation(S)
            results.append(result)
        
    with open(file_out, 'w') as fout:
        for case, result in enumerate(results, 1):
            line = 'Case #{}: {}\n'.format(case, result)
            fout.write(line)
            
            
    

if __name__ == '__main__':
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    main(file_in, file_out)
