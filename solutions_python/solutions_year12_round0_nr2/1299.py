# author: Philip Ting
# Google Code Jam

def main():
    with open('B-large.in', encoding='utf-8') as r:
        with open('output.txt', mode='w', encoding='utf-8') as w:
            
            T = int(r.readline()[:-1])
            
            for nth in range(T):
                temp = [int(item) for item in r.readline()[:-1].split(' ')]
                N = temp[0]
                S = temp[1]
                p = temp[2]
                t = temp[3:]
                
                # formula - a given total score should give highest
                # individual score p = (score + 2) // 3
                # or p = (score + 4) // 3 if suprising
                #
                # Suprising does not affect 0,1,29,30
                
                count = 0
                t.sort()
                for ti in t:
                    #print("ti: " + str(ti) + ", p:" + str(p) + ", S:" + str(S))
                    if ti == 0:
                        if 0 >= p:
                            #print("added in 0")
                            count += 1
                    elif ti == 1:
                        if 1 >= p:
                            #print("added in 1")
                            count += 1
                    elif ti == 30 or ti == 29:
                        if 10 >= p:
                            #print("added in 29/30")
                            count += 1
                    elif S:
                        if (ti+4)//3 >= p:
                            #print("added in S")
                            count += 1
                            S -= 1
                    elif (ti+2)//3 >= p:
                        count += 1
                        #print("added without S")
                
                # output to file
                w.write('Case #' + str(nth+1) + ': ' + str(count) + '\n')
    
if __name__ == "__main__":
    main()
