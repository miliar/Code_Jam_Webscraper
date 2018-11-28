
def main():
    t = int(raw_input())
    for case in range(1,t+1):
        prev_time = {'B':0, 'O':0}
        prev_pos  = {'B':1, 'O':1}
        inp = raw_input().split()
        N = int(inp[0])
        time = [ 0  for x in range(N) ]
        typ=[]
        dist=[]
        inp = inp[1:]
        for i in range(len(inp)):
            if i%2==0:
                typ.append(inp[i])
            else:
                dist.append(int(inp[i]))

        time[0] = dist[0]

        if typ[0]  == 'B':
            prev_time['B'] = time[0]
            prev_pos['B'] = dist[0]
        else:
            prev_time['O'] = time[0]
            prev_pos['O'] = dist[0]

        for i in range(1,N):
            if typ[i] == typ[i-1]:
                time[i] = time[i-1]+1+abs(dist[i]-prev_pos[typ[i]])
                prev_time[typ[i]] = time[i]
                prev_pos[typ[i]] = dist[i]
            else:
                time[i] = time[i-1]+1+max(0,abs(dist[i]-prev_pos[typ[i]])-abs(prev_time['O']-prev_time['B']))
            prev_time[typ[i]] = time[i]
            prev_pos[typ[i]] = dist[i]

        print "Case #" + str(case) + ": " + str(time[N-1])


if __name__ == "__main__":
    main()
            
                

        
    

