def main():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_cases = int(input())
    for case in range(num_cases):
        last_num = input()
        chars = list(last_num)
        num = ''

        for i in range(len(chars))[::-1]:
            if i != 0 and chars[i] < chars[i - 1]:
                num = '9' * (len(chars) - i)
                # chars[i - 1] = chr(ord(chars[i - 1]) - 1)
                chars[i - 1] = numbers[int(chars[i - 1]) - 1]
            else:
                num += chars[i]

        print('Case #{0}: {1}'.format(case + 1, int(num[::-1])))


main()
