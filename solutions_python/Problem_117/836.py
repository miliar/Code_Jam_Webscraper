def pattern_is_possible(lawn,lines,columns):
    lawn2 = []
    for i in range(lines):
        lawn2.append([max(lawn[i])]*columns)
    for j in range(columns):
        max_el = max(lawn[i][j] for i in range(lines))
        for i in range(lines):
            if max_el<=lawn2[i][j]:
                lawn2[i][j] = max_el
            if(lawn2[i][j]!=lawn[i][j]):
                return False
    return True

def main():
    fout = open("lawnmower.out",'w')
    with open("lawnmower.in",'r') as fin:
        case_numbers = int(fin.readline().strip())
        for q in range(case_numbers):
            n,m = map(int,fin.readline().strip().split())
            lawn = []
            for i in range(n):
                lawn.append(list(map(int,fin.readline().strip().split())))
            if(pattern_is_possible(lawn,n,m)):
                fout.write("Case #{}: {}\n".format(q+1,"YES"))
            else:
                fout.write("Case #{}: {}\n".format(q+1,"NO"))

    fout.close()
if __name__ == '__main__':
    main()
