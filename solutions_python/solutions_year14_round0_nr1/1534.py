def main():
    T=int(raw_input())
    for case in range(T):
        row = []
        guess1=int(raw_input())
        row.append([])
        for i in range(0,4):
            row[0].append(raw_input().split(' '))
        guess2=int(raw_input())
        row.append([])
        for i in range(0,4):
            row[1].append(raw_input().split(' '))
        candidates = row[0][guess1-1]
        count = 0
        results=[]
        for x in candidates:
            if x in row[1][guess2-1]:
                results.append(x)
                count+=1
        if count == 1:
            print 'Case #%d: %s'%(case+1,results[0])
        elif count >1:
            print 'Case #%d: Bad magician!'%(case+1)
        elif count == 0:
            print 'Case #%d: Volunteer cheated!'%(case+1)



if __name__ == '__main__':
    main()
