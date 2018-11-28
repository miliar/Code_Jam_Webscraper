from collections import Counter
def main():
    fout = open("tik_tak_toe.out",'w')
    with open("tik_tak_toe.in",'r') as fin:
        case_numbers = int(fin.readline().strip())
        for g in range(case_numbers):
            l = []*4
            for i in range(4):
                l.append(fin.readline().strip())
            fin.readline()
            x_won = False
            o_won = False
            punct = 0
            for i in range(4):
                line = Counter(l[i])
                if line['X'] == 4 or (line['X'] == 3 and line['T']==1):
                    x_won = True
                elif line['O'] == 4 or (line['O'] == 3 and line['T']==1):
                    o_won = True
                punct += line['.']
            for j in range(4):
                col = Counter([l[i][j] for i in range(4)])
                if col['X'] == 4 or (col['X'] == 3 and col['T']==1):
                    x_won = True
                elif col['O'] == 4 or (col['O'] == 3 and col['T']==1):
                    o_won = True

            right_diag = Counter(l[q][q] for q in range(4))
            if right_diag['X'] == 4 or (right_diag['X'] == 3 and right_diag['T']==1):
                x_won = True
            elif right_diag['O'] == 4 or (right_diag['O'] == 3 and right_diag['T']==1):
                o_won = True
            left_diag = Counter([l[q][3-q] for q in range(4)])
            if left_diag['X'] == 4 or (left_diag['X'] == 3 and left_diag['T']==1):
                x_won = True
            elif left_diag['O'] == 4 or (left_diag['O'] == 3 and left_diag['T']==1):
                o_won = True

            if(not punct and not x_won and not o_won):
                fout.write("Case #{}: {}\n".format(g+1," Draw"))
            elif(x_won):
                fout.write("Case #{}: {}\n".format(g+1," X won"))
            elif(o_won):
                fout.write("Case #{}: {}\n".format(g+1," O won"))
            else:
                fout.write("Case #{}: {}\n".format(g+1," Game has not completed"))









    fout.close()
if __name__ == '__main__':
    main()
