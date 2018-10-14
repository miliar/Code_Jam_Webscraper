f = open("input")
f_out = open('output', 'w')

def isFairSqPalindrom(num):
    str_num = str(num)
    len_str_num = len(str_num)
    if str_num[:len_str_num/2][::-1] != str_num[-(len_str_num/2):]:
        if len_str_num > 1:
            return False
    
    num = num ** 0.5
    if int(num) != num:
        return False
    str_num = str(int(num))
    len_str_num = len(str_num)
    if str_num[:len_str_num/2][::-1] != str_num[-(len_str_num/2):]:
        if len_str_num > 1:
            return False
    return True

for i in range(int(f.readline())):
    n, m = f.readline()[:-1].split(' ')
    n = int(n)
    m = int(m)
    
    cnt = 0
    for number in xrange(n, m + 1):
        if isFairSqPalindrom(number) == True:
            cnt += 1
            
    f_out.write("Case #%i: %i\n" % (i + 1, cnt))

f.close()
f_out.close()
print "done"