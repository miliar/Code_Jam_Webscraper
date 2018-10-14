__author__ = 'heng.lh'


in_file = open('in.txt')
out_file = open('out.txt','w')

def fan(cake):
    if cake == '-':
        return '+'
    else:
        return '-'


cnt = 0
num = 0
for line in in_file:
    arr = line.split(' ')
    if len(arr) == 1:
        cnt = int(arr[0])
    else:
        num += 1
        pancakes = list(arr[0])
        k = int(arr[1])
        i = 0
        flag = True
        result = 0
        while i < len(pancakes):
            if pancakes[i] == '-':
                if i + k > len(pancakes):
                    flag = False
                    break
                result += 1
                for idx in range(k):
                    pancakes[idx + i] = fan(pancakes[idx + i])
            if flag == False:
                break
            i += 1
        if flag:
            out_file.write('Case #%d: %d\n' % (num, result))
        else:
            out_file.write('Case #%d: IMPOSSIBLE\n' % num)

in_file.close()
