

def check(n):
    for i in range(len(str(n))-1):
        if str(n)[i] > str(n)[i+1]:
            return False
    return True

assert check(4)
assert check(129)
assert not check(990)

def solve2(txt):
    N = int(txt)
    answers = set()
    answers.add(N)
    N_str = str(N)
    for i,s in enumerate(N_str):
        if s!="0":
            tmp_str = N_str[:i]+str(int(s)-1)+"9"*(len(N_str)-i-1)
            answers.add(int(tmp_str))
    ans = max([answer for answer in answers if check(answer)])
    print(ans)
    #print( answers)


def solve(input_text):
    N = int(input_text)
    for i in range(len(str(N))):
        if check(N):
            break

        if str(N)[-(i+1)] > max((str(N)[:-(i+2)])) :
            N -= (int(str(N)[-(i+1)] )+1) *10**i
            print(N)
    print(N)
    return

    while not check(N):
        for i in reversed(range(len(str(N))-1)):
            if str(N)[i] > str(N)[i+1]:
                N -= 10**(len(str(N))-i-2)
                print(N)
                #N -=1
                break
    print(N)


for i in range(int(input())):
    print("Case #{}:".format(i+1),end=" ")
    solve2(input())