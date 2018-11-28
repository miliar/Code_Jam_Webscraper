def C(input):
    def getchar(i_c, i_start, ans):
        if i_c == len(s):
            ans[0] += 1
            return
        ind = input.find(s[i_c], i_start)
        while ind != -1:
            getchar(i_c + 1, ind, ans)
            ind = input.find(s[i_c], ind + 1)

    s = 'welcome to code jam'
    ans = [0]
    getchar(0, 0, ans)
    return "%04d" % ans[0]

if __name__ == '__main__':
    #str_in = 'A-small-attempt1.in'
    str_in = 'C-small-attempt0.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')

    for i, input in enumerate(open(str_in)):
        input = input.strip()
        if i == 0:
            continue
        f_out.write('Case #' + str(i) + ': ' + C(input) + '\n')
        #f_out.write('Case #' + str(i) + ': \n' + B(input))
        #f_out.write('Case #' + str(i) + ': ' + C(input) + '\n')

    f_out.close()

