def main():
    cases = int(input())

    for i in range(1, cases+1):
        stack, flipper = input().split()
        s = "Case #" + repr(i) + ":"
        print(s, solve(stack,flipper))

def solve(stack, flipper):
    flip_count = 0
    stack = list(stack)
    if check_good(stack):
        return 0

    for i in range(0, len(stack)-int(flipper)+1):
        if(stack[i] == '-'):
            for j in range(0,int(flipper)):
                if stack[i+j] == '+':
                    stack[i+j] = '-'
                else:
                    stack[i+j] = '+'
            flip_count += 1

    if check_good(stack):
        return flip_count
    else:
        return "IMPOSSIBLE"
    


def check_good(stack):
    for s in stack:
        if s == '-':
            return False
    return True





if __name__ == '__main__':
    main()
