"""
    TIDY
"""
def main():
    """Main
    Start with this main function
    """
    # Pancake flipper
    total_line = int(input())
    for i in range(1, total_line+1):
        num = input()
        num = int(num)
        ans = last_tidy(num)
        print('Case #{}: {}'.format(i, str(ans)))

def last_tidy(num):
    """last_tidy
    Find last tidy number
    Args:
        num: Last number
    Returns: Last tidy number
    Raises:
    """
    num_str = str(num)
    for i in reversed(range(1, len(num_str))):
        if is_higher_in(num_str[:i], num_str[i]):
            num_str = str(int(num_str[:i])-1) + '9' + '9'*len(num_str[i+1:])

    return int(num_str)

def is_higher_in(num, digit):
    num_str = str(num)
    for i in range(len(num_str)):
        if int(num_str[i]) > int(digit):
            return True

    return False


if __name__ == '__main__':
    main()
