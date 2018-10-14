#%%
with open("B-small-attempt1.in") as fr:
    T = int(fr.readline())
    Ns = []
    for i in range(T):
        Ns.append(fr.readline()) # can't use int since the large case up to 10**18 =~ 2**60

def check(n):
    s_n = str(n)
    for i in range(len(s_n)-1):
        if int(s_n[i]) > int(s_n[i+1]):
            return False
    return True
def solutionB_small(N):
    num = int(N)
    while num > 0:
        if '0' not in str(num):
            if check(str(num)):
                return num
        num -= 1


def solutionB_large(N):
    return N

with open('ans.txt', 'w', encoding='utf8') as fw:
    for index, n in enumerate(Ns, start=1):
        largest_tidy = solutionB_small(n)
        ans = "Case #{}: {}\n".format(index,largest_tidy)
        fw.write(ans)