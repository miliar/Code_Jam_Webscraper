FILE = 'B-small-attempt0.in'

def neat(num):
    for j in range(num, 0, -1):
        num_str = str(j)
        yes = True

        for k in range(1,len(num_str)):
            if num_str[k] < num_str[k-1]:
                yes = False
                break

        if yes:
            return j

def main():
    file = open(FILE).readlines()

    for i in range(1, len(file)):
        num = int(file[i].strip())

        neat_num = neat(num)

        print('Case #{}: {}'.format(i, neat_num))
        
main()
