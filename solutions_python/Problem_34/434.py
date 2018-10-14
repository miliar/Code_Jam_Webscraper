def generate_word(case,word_length):
    tmp = case.split(')')
    try:
        tmp.remove('')
    except:
        pass

    c = []
    for t in tmp:
        x = t.find('(')
        if x == 0 or x == -1:
            c.append(t)
        else:
            t1, t2 = t.split('(')
            c.append(t1)
            c.append('(' + t2)
    print 'c',c

    ans = []
    for w in c:
        if w[0] == '(': # random letter
            ans.append([a for a in w[1:]])
        else:
            for a in w:
                ans.append([a])
    #print 'ans',ans,len(ans)
    if len(ans) != word_length:
        return []

    return ans

if __name__ == '__main__':
    try:
        f = open('A-large.in')
        w = open('A-large.out','w')
        #f = open('test.txt')
        #w = open('test.out','w')

        word_length, word_count, n_case = map(int,f.readline().strip().split())
        word_list = []
        ans_list = []

        for i in range(word_count):
            word = f.readline().strip()
            word_list.append(word)

        for i in range(1,n_case+1):
            case = f.readline().strip()
            possible_word_list = generate_word(case,word_length)
            ans = 0
            if possible_word_list == []:
                pass
            else:
                for word in word_list:
                    c = True
                    for j in range(word_length):
                        if possible_word_list[j].count(word[j]) == 0:
                            c = False
                            break
                    if c:
                        ans += 1

            #print 'ans',ans
            if i == n_case:
                w.write('Case #' + str(i) + ': ' + str(ans))
            else:
                w.write('Case #' + str(i) + ': ' + str(ans) + '\n')

        f.close()
        w.close()
        #w = open('A-small-practice.out','w')
        #w = open('A-large-practice.out','w')
    except Exception,ex:
        print str(ex)
        f.close()
        w.close()


