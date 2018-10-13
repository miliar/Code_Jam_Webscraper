from fractions import gcd

def int_input():
    return int(raw_input())

def list_int_input():
    return map(int, raw_input().split())

def get_years():
    years = list_int_input()
    del years[0]
    years = list(set(years))
    years.sort(reverse=True)
    return years

def get_diff(years):
    diff = list()
    for i, y in enumerate(years):
        if i > 0:
            d = years[i-1] - years[i]
            if d > 0:
                diff.append(d)
    diff.sort()
    return diff

def get_diff_gcd(diff):
    diff_gcd = None
    for d in diff:
        if diff_gcd is None:
            diff_gcd = d
        else:
            diff_gcd = gcd(diff_gcd, d)
    return diff_gcd

def dividable(years, diff_gcd):
    for y in years:
        if y % diff_gcd != 0:
            return False
    return True

def main():
    for c in range(int_input()):
        years = get_years()
        diff = get_diff(years)
        diff_gcd = get_diff_gcd(diff)
        if diff_gcd == 1:
            answer = 0
        elif dividable(years, diff_gcd):
            answer = 0
        else:
            answer = diff_gcd - (years[0] % diff_gcd)
        print 'Case #%d: %d' % (c+1, answer)

main()
