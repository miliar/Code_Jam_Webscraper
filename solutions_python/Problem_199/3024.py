def solve(s, k):
    s = [True if x=='+' else False for x in s]
    flip = 0
    for i in range(len(s)-k+1):
        if not s[i]:
            target = s[i:i+k]
            flipped = [not x for x in target]
            s[i:i+k] = flipped
            flip = flip + 1

    if all(s):  return str(flip)
    else:       return "IMPOSSIBLE"

if __name__ == "__main__":
    test_cases_num = int(input())
    for case_num in range(1, test_cases_num+1):
        # given = input()
        given = input().split()
        # print (given.split())
        print("Case #%i: %s" % (case_num, solve(given[0], int(given[1]))))