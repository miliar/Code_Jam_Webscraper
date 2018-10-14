def main():
    outfile = open('output.txt', 'w')
    infile = open('input.txt', 'r')

    n = int(infile.readline())
    for i in range(n):
        div = infile.readline().split('/');
        P = int(div[0]);
        Q = int(div[1]);
        
        if (Q&(Q-1)!=0):
            outfile.write('Case #' + str(i+1) + ': impossible\n')
        else:
            for gen in range(1,40):
                if (P>Q):
                    outfile.write('Case #' + str(i+1) + ': impossible\n')
                    break
                elif ((2*P)>=Q):
                    outfile.write('Case #' + str(i+1) + ': ' + str(gen) + '\n')
                    break
                else:
                    Q = Q/2;
    
    infile.closed
    outfile.closed

if __name__ == "__main__":
    main()
