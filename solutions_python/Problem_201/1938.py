def process(n, k):
    empties = []    
    empties.append(n)
    for i in range(k - 1):
        size = empties.pop()
        size -= 1
        left_empty = size / 2
        right_empty = size - left_empty
        empties.append(left_empty)
        empties.append(right_empty)
        empties.sort()    

    size = empties.pop()
    size -= 1
    left_empty = size / 2
    right_empty = size - left_empty
                 
    return (right_empty, left_empty)
'''
print(process(4, 2) == (1, 0))
print(process(5, 2) == (1, 0))
print(process(6, 2) == (1, 1))
print(process(1000, 1000) == (0, 0))
print(process(1000, 1) == (500, 499))

print(process(10, 1) == (5, 4))
print(process(10, 2) == (2, 2))
print(process(10, 3) == (2, 1))
print(process(10, 4) == (1, 0))
print(process(10, 5) == (1, 0))
print(process(10, 6) == (1, 0))
print(process(10, 7) == (0, 0))
print(process(10, 8) == (0, 0))
print(process(10, 9) == (0, 0))
print(process(10, 10) == (0, 0))
'''


f = open('/sdcard/Download/C-small-1-attempt0.in')
#f = open('/sdcard/Download/C-large-practice.in')
f_out = open('/sdcard/Download/C-small-out.txt', 'w')
#f_out = open('/sdcard/Download/C-large-practice-out.txt', 'w')
s = f.readlines()
tc_num = int(s[0])
for i in range(tc_num):
    a, b = [int(x) for x in s[i + 1].split()]
    answer = process(a, b)
    f_out.write("Case #%d: %d %d\n" % (i + 1, answer[0], answer[1]))
f.close()
f_out.close()

