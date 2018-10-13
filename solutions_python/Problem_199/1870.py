import random
def process(s, k):
    flip_num = 0
    l = list(s)
    cake_size = len(l)
    for i in range(cake_size):
        if l[i] == '-':
            if i + k - 1 < cake_size:
                for j in range(i, i + k):
                    l[j] = '-' if l[j] == '+' else '+'
                flip_num += 1    
            else:
                #print(-1)
                return -1
    #print(flip_num)
    return flip_num 
             
  
def test():
    print(process('---+-++-', 3) == 3)
    print(process('+++++', 4) == 0)
    print(process('-+-+-', 4) == -1)
    
    for x in range(100):
        print(process(''.join(['+' if random.randint(0,2) == 0 else '-' for x in range(1000)]), 1) == 1)

#test()

f = open('/sdcard/Download/A-large.in')
#f = open('/sdcard/Download/C-large-practice.in')
f_out = open('/sdcard/Download/A-large-out.txt', 'w')
#f_out = open('/sdcard/Download/C-large-practice-out.txt', 'w')
s = f.readlines()
tc_num = int(s[0])
for i in range(tc_num):
    a, b = s[i + 1].split()
    answer = process(a, int(b))
    print("Case #%d: %s" % (i + 1, 'IMPOSSIBLE' if answer == -1 else answer))
    f_out.write("Case #%d: %s\n" % (i + 1, 'IMPOSSIBLE' if answer == -1 else answer))
f.close()
f_out.close()
