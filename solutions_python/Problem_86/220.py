def get_no_chess_boards(v2,used, M, N):
    chess_boards = []
    for i in xrange(M):
        print v2[i]
    answer = 0
    i=0
    while i < M:
        j = 0
        while j < N:
            width = find_largest_chess(v2, i, j, used, M, N)
            print j,i, width
            chess_boards.append(width)
            j += width+1            
        i += 1
    count = []
    for i in xrange(N+1):
        count.append(0)    
    for i in xrange(len(chess_boards)):
          count[chess_boards[i]+1] += 1
        
    return len(chess_boards), count
        
def getHar(N, L, H, har):
    i = L
    while i <= H:
        for j in xrange(N):
            if i%har[j] == 0 or har[j]%i == 0:
                if j == N-1:
                    return i
            else:
                break
        i += 1
        
    return i
    
def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("C-small-attempt0.out", "w")
    
    for test_case_counter in xrange(test_case_count):
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        N = int(lines1[0])
        L = int(lines1[1])
        H = int(lines1[2])
        har = []
        lines2 = (input_file.readline().replace('\n','')).split(' ')
        for i in xrange(N):
            har.append(int(lines2[i]))
        
        final = getHar(N, L, H, har)
         
        output_file.write("Case #"+str(test_case_counter+1)+": ")
        if final > H:
            output_file.write("NO\n")
        else:
            output_file.write(str(final)+ '\n')

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("C-small-attempt0.in")
    prepare_input(input_file)
