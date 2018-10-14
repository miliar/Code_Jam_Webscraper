import difflib, collections

def solve(array):
    ans = check(array)
    if not check(array):
        return -1

    count = 0

    I = [0 for a in array]
    for char in ans:

        cnt_char = [0 for a in array]

        for i in xrange(len(array)):
            while I[i] < len(array[i]) and array[i][I[i]] == char:
                cnt_char[i] += 1
                I[i] += 1


        # print cnt_char

        short = 1000
        for i in xrange(1, max(cnt_char) + 1):
            summ = 0
            for cc in cnt_char:
                summ += abs(cc - i)
            short = min(short, summ)

        count += short




    # ans_i = 0
    # while k < 100:
    #     k +=1
    #     cnt = collections.Counter()
    #
    #     flag = False
    #     for i in xrange(len(array)):
    #         if I[i] >= len(array[i]):
    #             flag = True
    #             break
    #         cnt[array[i][I[i]]] += 1
    #     if flag:
    #         break
    #
    #     # if len(cnt) == 1:
    #     #     ans_i += 1
    #     common = cnt.most_common(1)[0][0]
    #
    #
    #     print cnt, I, common, count, ans[ans_i]
    #
    #     if common == ans[ans_i]:
    #         print 'susumu',
    #         # susumu
    #         for i in xrange(len(array)):
    #             if array[i][I[i]] == common:
    #                 I[i] += 1
    #             else:
    #                 count += 1
    #     else:
    #         for i in xrange(len(array)):
    #             if array[i][I[i]] != common:
    #                 I[i] += 1
    #                 count +=1
    #     prev = common

    return count

def check(array):
    re = array[0]
    prev = ''
    ans = ''
    for i in xrange(len(re)):
        if not prev:
            prev = re[i]
            ans += re[i]
        else:
            if prev != re[i]:
                ans += re[i]
                prev = re[i]

    prev = ''
    for str in array[1:]:
        s = ''
        for i in xrange(len(str)):
            if not prev:
                prev = str[i]
                s += str[i]
            else:
                if prev != str[i]:
                    s += str[i]
                    prev = str[i]
        if s != ans:
            return False
    return ans


if __name__ == "__main__":
    with open('inputA.txt', 'r') as infile, open('outputA.txt', 'w') as outfile:
        data = []
        for line in infile:
            data.append(line.split())

        N = int(data[0][0])
        data.pop(0)

        for n in xrange(N):
            T = int(data[0][0])
            data.pop(0)
            array = []
            for t in xrange(T):
                array.append(data.pop(0)[0])
            ans = solve(array)
            if ans < 0:
                str = "Case #{0}: {1}\n".format(n+1, "Fegla Won")
            else:
                str = "Case #{0}: {1}\n".format(n+1, ans)
            print str
            outfile.write(str)
