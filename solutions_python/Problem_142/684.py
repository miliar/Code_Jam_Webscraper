INPUT = "A-small-attempt2.in"
OUTPUT = "A-small-attempt2.out"
NEWLINE = "\n"
DEBUG = False

import math

def words_equal(words):
    flag = True
    for i,_ in enumerate(words):
        if i==0:
            continue
        if words[i] != words[i-1]:
            flag = False
    return flag

def diff_letters(words):
    res = []
    for word in words:
        count = 1
        j = 1
        while j < len(word):
            if word[j] != word[j-1]:
                count += 1
            j += 1
        res.append(count)
    return res

def same(l):
    c = l[0][0]
    for t in l:
        if t[0] != c:
            if DEBUG:
                print c
            return False
    return True

def get_next(words,t):
    res = []
    for w in words:
        j = 1
        count = 1
        while count < t:
            if j >= len(w):
                tup = (None, None) 
                res.append(tup)
            if w[j] != w[j-1]:
                count += 1
            j += 1
        c = w[j-1]
        count = 1
        if j >= len(w):
            tup = (c,count)
            res.append(tup)
        while j<len(w):
            if w[j] != w[j-1]:
                tup = (c,count)
                res.append(tup)
                break
            count += 1
            if (j == len(w) - 1):
                tup = (c,count)
                res.append(tup)
            j += 1 
    return res
            
  
if __name__ == '__main__':
    in_file = file(INPUT, "r")
    out_file = file(OUTPUT, "w")
    
    lines = in_file.readlines()
    cases_num = int(lines[0])
    
    out_lines = []
    data = lines[1:]
    counter = 0    
    for case in range(1 , cases_num+1):
        i = case - 1
        N = int(data[counter])
        counter += 1
        result = 0
        words = [''] * N
        for j in range(N):
            tmp = data[counter]
            counter+=1
            words[j] = tmp.strip()
        if DEBUG:
            print ("case %d: " % case) + str(words)
        
        if words_equal(words):
            res = "Case #%d: 0" % case
            if DEBUG:
                print res
            out_lines += ("Case #%d: 0" % case) + NEWLINE
            continue
        
        d = diff_letters(words)
        flag = True
        for i,_ in enumerate(d):
            if i==0:
                continue
            if d[i] != d[i-1]:
                flag = False
        
        if not flag:
            res = "Case #%d: Fegla Won" % case
            if DEBUG:
                print res
            out_lines += res + NEWLINE
            continue
                
        
        t = d[0]
        words_num = len(words)
        total = 0
        for j in range(1,t+1):
            next = get_next(words, j)
            flag = True
            if not same(next):
                flag = False
                res = "Case #%d: Fegla Won" % case
                if DEBUG:
                    print res
                out_lines += res + NEWLINE
                break               
            sum = 0
            r1 = 0
            for t in next:
                sum += t[1]
            c1 = sum / words_num
            for t in next:
                r1 += math.fabs(t[1] - c1)
            c2 = sum / words_num + 1
            r2 = 0
            for t in next:
                r2 += math.fabs(t[1] - c2)
            total += min(r1,r2)
        if DEBUG:
            print total
        if not flag:
            continue
        res = "Case #%d: %d" % (case, int(total))
        out_lines += res + NEWLINE
               
            
        
        
        
            
        
       
    out_file.writelines(out_lines)
    in_file.close()
    out_file.close()
    print 'done problem A'
        