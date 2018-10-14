inputfile = r'A-large.in'
outputfile = r'A-large.out'

#input
def input_data():
    import os
    os.chdir(r'C:\codejam')
    FILENAME = inputfile 
    f = open(FILENAME)
    lines = f.readlines()
    f.close()
    return lines

#output
def output_data(ans):    
    fout = open(outputfile, 'wt')
    print(ans, file = fout)
    fout.close()

def comp(A):
    ans = []
    for ir in range(len(A)):
        emppos = []
        e = list(A[ir][:-1])
        if set(list(e)) != set(['?']):
            for ic in range(len(e)):
                if e[ic] == '?':
                    emppos.append(ic)
                else:
                    char = e[ic]
                    while len(emppos) > 0:
                        e[emppos.pop()] = char
            while len(emppos) > 0:
                e[emppos.pop()] = char
        ans.append(''.join(e))

    emprow = []
    for ir in range(len(ans)):
        if '?' in ans[ir]:
            emprow.append(ir)
        else:
            sent = ans[ir]
            while len(emprow) > 0:
                ans[emprow.pop()] = sent
    while len(emprow) > 0:
        ans[emprow.pop()] = sent
    return ans

if __name__ == '__main__':
    lines = input_data()

    #calc
    T = int(lines.pop(0)[:-1])
    ans = ''    
    for i in range(T):
        R, C = map(int, lines.pop(0)[:-1].split())
        list_cake = [lines.pop(0) for i in range(R)]
        list_ans = comp(list_cake)
        ansline = 'Case #' + str(i+1) + ':\n'
        ans += ansline
        for e in list_ans:
            ans += e + '\n'
    output_data(ans)
    
