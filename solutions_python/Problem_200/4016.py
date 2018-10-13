def return_last_tidy(n, lim):
    s = str(n)
    i = 1
    curr = s[0]
    tidy=True
    while True and i<lim:
        if not curr <= s[i]:
            # print('breaking', i, curr, s[i])
            tidy=False
            break
        curr = s[i]
        i+=1
    if tidy:
        return int(s)
    else:
        # print('not tidy')
        # print('s[:i-1]', s[:i-1])
        # print('s[i-1]', s[i-1])
        news = s[:i-1]+str(int(s[i-1])-1)
        # print('news', news)
        for i in range(i, len(s)):
            news += '9'
        # print('calling again', i-1)
        return return_last_tidy(int(news), i)

# n = 111111111111111110
# n = 132
# print(return_last_tidy(n, len(str(n))))

def main():
    t = int(input())
    for x in range(t):
        n = int(input())
        soln = return_last_tidy(n, len(str(n)))
        print("Case #{}: {}".format(x+1, soln))

main()
