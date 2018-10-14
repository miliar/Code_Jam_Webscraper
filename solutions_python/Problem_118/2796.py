import sys

def read_cases(path):
    f = open(path)
    lines_count = int(f.readline())
    lines = [line.strip() for line in f.readlines()]
    for i in range(lines_count):
        yield lines[i]

def work_on_case(case):
    start, end = [int(d) for d in case.split(" ")]
    return fair_and_squares(start, end)

def fair_and_squares(start, end):
    start_root = int(start**0.5)
    if start_root**2 < start:
        start_root = start_root + 1
    end_root = int(end**0.5)
    total = 0
    for p in palindromes_from(start_root, end_root):
        num = p**2
        if is_palindrome(num):
            total += 1
    return total

def palindromes_from(start, end):
    for num in range(start, end+1):
        if (is_palindrome(num)):
            yield num

def is_palindrome(num):
    s = str(num)
    return all([s[i] == s[-i-1] for i in range(len(s)//2+1)])
    

if __name__ == "__main__":
    total_result = open(r"C:\temp\C-small-result.txt", "w")
    for i, case in enumerate(read_cases(r"C:\temp\C-small-attempt0.in")):
        result = work_on_case(case)
        print("Case #%d: %s" % (i+1, result), file=total_result)
    total_result.close()
