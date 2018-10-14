def main():
    T = int(input().strip())

    for t in range(T):
        N = list(input().strip())

        for i in range(len(N)-1, 0, -1):
            if int(N[i]) < int(N[i-1]):
                N[i-1] = str(int(N[i-1])-1)
                j = i
                while j < len(N) and N[j] is not '9':
                    N[j] = '9'
                    j += 1
        print('Case #{}: {}'.format(t+1, int(''.join(N))))

if __name__ == '__main__':
    main()
