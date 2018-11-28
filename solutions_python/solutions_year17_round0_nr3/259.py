testcase = int(input())

# N -> (N-1)/2 + O + N/2

for tc in range(1, testcase+1):

    N, K = [int(s) for s in input().split(" ")]
    searchlist = [(N, 1)] # N empty stall, 1 person is going
    #searchlist = [(N, 1), (N//2, 1), ((N-1)//2, 1)]
    searchlist_index_start = 0
    searchlist_index_end = 1
    totalpeople = 1

    
    while totalpeople < K:

        currentsearchlist = []
        currentsearchdic = {}
        for searching in range(searchlist_index_start, searchlist_index_end):
    
            tempnum = searchlist[searching][0]
            tempppl = searchlist[searching][1]
            
            if currentsearchlist.count(tempnum//2) == 0:
                currentsearchlist.append(tempnum//2)
                currentsearchdic[tempnum//2] = tempppl
            else:
                currentsearchdic[tempnum//2] += tempppl

            if currentsearchlist.count((tempnum-1)//2) == 0:
                currentsearchlist.append((tempnum-1)//2)
                currentsearchdic[(tempnum-1)//2] = tempppl
            else:
                currentsearchdic[(tempnum-1)//2] += tempppl

        currentsearchlist.sort()
        currentsearchlist.reverse()

        for currentelements in currentsearchlist:
            searchlist.append((currentelements, currentsearchdic[currentelements]))
            totalpeople += currentsearchdic[currentelements]

        searchlist_index_start = searchlist_index_end
        searchlist_index_end = len(searchlist)
        
        
        '''
        nextN1 =  searchlist[searchlist_index + 1][0]      // 2
        nextN2 = (searchlist[searchlist_index + 1][0] - 1) // 2
        ppl1 = searchlist[searchlist_index+0][1]
        ppl2 = searchlist[searchlist_index+1][1]
        searchlist.append((nextN1, ppl1))
        searchlist.append((nextN2, ppl1 + 2*ppl2))
        '''
    #print(searchlist)

    s = 0
    ansindex = 0
    while s < K:
        s += searchlist[ansindex][1]
        ansindex += 1

    ansindex -= 1
    ans1 = str( searchlist[ansindex][0]    // 2)
    ans2 = str((searchlist[ansindex][0]-1) // 2)
    print("Case #"+str(tc)+": "+ans1+" "+ans2)
