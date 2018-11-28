# https://github.com/shang-lin/gcj/

from gcj import CodeJam

def is_tidy(num):
    """
    >>> is_tidy(7)
    True
    >>> is_tidy(321)
    False
    >>> is_tidy(132)
    False
    >>> is_tidy(129)
    True
    >>> is_tidy(99999999999999999)
    True
    """
    tidy = True
    if num < 10:
        return True
    
    n = num // 10
    prev_last_digit = num % 10
    while n > 0: 
        last_digit = n % 10
        if last_digit > prev_last_digit:
            #print('{} {}'.format(last_digit, prev_last_digit))
            return False
        prev_last_digit = last_digit
        n = n // 10
    return True

def last_tidy(n):
    if is_tidy(n):
        return n
    for i in range(n, 1, -1):
        if is_tidy(i):
            return i

if __name__ == "__main__":
    codejam = CodeJam(last_tidy)
    codejam.run()
