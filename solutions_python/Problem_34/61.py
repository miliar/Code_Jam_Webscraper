# Code Jam Qualifier
# 2/9/2009

inname = 'E:\A.in'

fin = open(inname, 'r')
fout = open('E:\A.out.txt', 'w')

lines = fin.readlines()

[l, d, n] = [int(x) for x in lines[0].split()]

print([l, d, n])

words = {}

def count_poss(st, cur_dict):
    if len(st) == 1:
        if st in cur_dict:
            return 1
    elif st[0] == '(':
        end_par = st.find(')')
        return sum([count_poss(s + st[end_par + 1:], cur_dict) for s in st[1:end_par]])
    elif st[0] in cur_dict:
        return count_poss(st[1:], cur_dict[st[0]])
    return 0

for i in range(1, d + 1):
    print('word ' + str(i))
    word = lines[i].strip()
    cur_dict = words

    for w in word:
        if w in cur_dict:
            cur_dict = cur_dict[w]
        else:
            cur_dict[w] = {}
            cur_dict = cur_dict[w]

for i in range(1, n + 1):
    print(str(i) + ' of ' + str(n))
    test_case = lines[d + i].strip()
    fout.write('Case #' + str(i) + ': ' + str(count_poss(test_case, words)) + '\n')

fout.close()
fin.close()
    
    
