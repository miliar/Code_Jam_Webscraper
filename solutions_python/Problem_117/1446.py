'''
Template

@author: Mohammad
'''

def main():  
    inn = open("B-small-attempt0.in", "r")
    out = open("out.txt", "w")
    T = int(inn.readline())
    for t in range(T):
        [N, M] = [int(n) for n in inn.readline().split()]
        board1 = []
        board2 = []
        heights = []
        visit = []
        for i in range(N):
            board1.append(list(int(n) for n in inn.readline().split()))
            heights = set(list(heights) + list(board1[i]))
            visit.append([False]*M)
        
        for j in range(M):
            board2.append([])
           
            for i in range(N):
                board2[j].append(board1[i][j])
        heights = sorted(list(heights))
        no = False
        hh = 0
        for h in heights:
            hh += 1
            for i in range(N):
                for j in range(M):
                    if not visit[i][j] and board1[i][j] == h :
                        if board1[i] == [h]*M:
                            visit[i] = [True]*M
                        elif board2[j] == [h]*N:
                            for k in range(N):
                                visit[k][j] = True
                        else:
                            no = True
                    if no:
                        break
                if no:
                    break
            if no:
                break
            else:
                visit = []
                for i in range(N):
                    visit.append([False]*M)
                    for j in range(M):
                        if hh < len(heights) and board1[i][j] == h:
                            board1[i][j] = heights[hh]
                    
        out.write('Case #' + str(t+1) + ': ')
        if no:
            out.write('NO')
        else:
            out.write('YES')
        out.write('\n')
    inn.close()
    out.close()
main()
