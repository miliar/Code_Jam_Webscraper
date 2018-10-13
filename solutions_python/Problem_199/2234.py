
def main():
    t = int(input())
    case = 1
    while t > 0:
        string, k = input().split()
        string = list(string)
        k = int(k)

        count = 0
        for i in range(len(string)):
            if i + k > len(string):
                break
            if string[i] == '-':
                count += 1
                for x in range(k):
                    if string[x + i] == '-':
                        string[x + i] = '+'
                    else:
                        string[x + i] = '-'

        if '-' in string[-k:]:
            answer = 'IMPOSSIBLE'
        else:
            answer = count

        print('Case #{case}: {answer}'.format(case=case, answer=answer))
        case += 1
        t -= 1


main()
