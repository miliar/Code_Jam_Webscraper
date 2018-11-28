for t in range(int(input())):
    (choice1,board1,choice2,board2) = (int(input())-1, [input().split() for i in range(4)],int(input())-1, [input().split() for i in range(4)])
    l=list(set(board1[choice1])&set(board2[choice2]))
    print('Case #{0}: {1}'.format(t+1,('Volunteer cheated!' if len(l)==0 else 'Bad magician!') if len(l)!=1 else l[0]))
    
