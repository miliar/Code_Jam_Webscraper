# problem b

if __name__ == '__main__':
    n_tests = int(raw_input())

    for ntest in range(1, n_tests+1):
        n, m = map(int, raw_input().split())
        recycled = 0
        recycled_ones = []
        
        for i in range(n, m + 1):
            for j in range(i + 1, m + 1):
                word1 = str(i)
                word2 = str(j)

                if set(word1) - set(word2) != set():
                    continue
                                
                for l in range(1, len(word1)):
                    left = word1[:l]
                    right = word1[l:]
                    
                    if right + left == word2 and (word1, word2) not in recycled_ones:
                        #print 'Comparing', word1, word2
                        #print 'left=', left
                        #print 'right=', right
                        #print 'go!'
                        recycled += 1
                        recycled_ones.append((word1, word2))
             
        print 'Case #%d: %d' % (ntest, recycled)