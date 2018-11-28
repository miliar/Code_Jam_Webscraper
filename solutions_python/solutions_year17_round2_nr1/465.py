

def speed(horses, d):
    eta = 0
    for di, si in horses:
        t = (d - di) / si
        eta = max(eta, t)
    return format(d/eta, '.6f')

def main():
    input_file = '/Users/tengg/Downloads/A-large.in'
    output_file = input_file+'.out'
    with open(input_file) as f, open(output_file, 'w') as o:
        t = int(f.readline())
        for i in range(1, t+1):
            d, n = map(int, f.readline().strip().split(' '))
            horses = []
            for _ in range(n):
                di, si = map(int, f.readline().strip().split(' '))
                horses.append((di, si))
            print(f'Case #{i}:', speed(horses, d), file=o)

if __name__ == '__main__':
    main()
