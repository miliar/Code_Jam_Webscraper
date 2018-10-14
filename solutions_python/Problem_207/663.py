#%%
def solutionB_small(n, Hs):
    for idx, i in enumerate(Hs):
        if i > (n-i):
            return "IMPOSSIBLE"
    color_map = dict(zip(range(6), "ROYGBV"))
    current_cnt = dict(zip("ROYGBV", range(6)))
    ans = ""
    max_idx = 0
    for idx, i in enumerate(Hs):
        if i>Hs[max_idx]:
            max_idx = idx

    max_color = color_map[max_idx]
    print(Hs)
    print(max_color)

    while Hs[current_cnt[max_color]]>0:
        ans += max_color
        cur_idx = current_cnt[max_color]
        Hs[cur_idx]-=1
        max_color = color_map[(cur_idx+2)%6] if Hs[(cur_idx+2)%6] > Hs[(cur_idx+4)%6] else color_map[(cur_idx+4)%6]
    print(n, ans)
    if len(ans) < n:
        return "IMPOSSIBLE"
    else:
        if ans[0] == ans[-1]:
            new_ans = ans[:-2]+ans[-1]+ans[-2]
            return new_ans
        else:
            return ans

with open("B-small-attempt2.in") as fr:
    with open('ans.txt', 'w', encoding='utf8') as fw:
        T = int(fr.readline())
        for j in range(T):

            H = [int(x) for x in fr.readline().split()]
            n = H[0]
            Hs = H[1:]
            ans = solutionB_small(n, Hs)
            ans = "Case #{}: {}\n".format(j+1, ans)
            fw.write(ans)
            print(ans)







"""
    for index, (c, k) in enumerate(zip(cakes, K), start=1):
        flip_times = solutionA(c, k)
        ans = "Case #{}: {}\n".format(index, flip_times if flip_times >= 0 else "IMPOSSIBLE")
        fw.write(ans)

Output format:
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE

"""
