def pancake_flip(N, k):
    st=[[N, 0]]
    vis=[]
    fin_ans="".join(['+'] * len(N))
    while True:
        if len(st)>0:
            tmp=st.pop(0)
            if tmp[0]==fin_ans:
                return tmp[1]

            vis.append(tmp[0])
            orig_tmp = tmp_state = tmp[0]
            count = tmp[1]
            tmp_state = list(tmp_state)
            flip = []
            d = {'+': '-', '-': '+'}
            for i in range(len(tmp_state)):
                if tmp_state[i] == '-':
                    for j in range(k):
                        if i-j >= 0 and k-j+i <= len(tmp_state):
                            y = list(orig_tmp)
                            for h in range(k):
                                y[h - j + i] = d[tmp_state[h - j + i]]
                            ans = "".join(y)
                            if ans not in flip:
                                if ans not in vis:
                                    flip.append([ans, count + 1])
                                    vis.append(ans)
            for i in flip:
                if i[0]==fin_ans:
                    return i[1]

                else:
                    for i in flip:
                        st.append(i)
        else:
            return "IMPOSSIBLE"

T = int(raw_input())
f = open('output1.txt', 'w')

for _ in range(1,T+1):
    N, k = map(str, raw_input().split())
    k = int(k)
    print "Case #" + str(_) + ":" + str(pancake_flip(N, k))
    f.write("Case #" + str(_) + ": " + str(pancake_flip(N, k)) + "\n")

f.close()
