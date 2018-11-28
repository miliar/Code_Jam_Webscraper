def main():
    ifile = open('input.txt', 'r')
    ofile = open('output.txt', 'w')
    n = int(ifile.readline())
    for i in range(0, n):
        p, k, l = map(int, ifile.readline().split(' '))
        freq = map(int, ifile.readline().split(' '))
        freq.sort()
        freq.reverse()
        print freq
        cnt = 0
        N = len(freq)
        for f in xrange(0, N):
            m = f / k
            cnt += (m + 1) * freq[f]
            
        print cnt
                         
        ofile.write('Case #%i: %i' %(i+1,cnt))
        if i != (n - 1):
            ofile.write('\n')
        
    ofile.close()
    print 'done'

if __name__ == '__main__':
  main()