
def make_string():
    s=input()+input()+input()+input()
    input() # toss unneeded line
    return ''.join(s.split())

def match(s,t):
    for e in s:
        if e!=t:
            return False
    return True

def try_this(s,u):
    t=s.replace('T', u)
    return match(t[0:4],u) or match(t[4:8],u) or match(t[8:12],u) or match(t[12:],u) or \
           match(t[0::4],u) or match(t[1::4],u) or match(t[2::4],u) or \
           match(t[3::4],u) or match(t[0::5],u) or match(t[3:15:3],u)

def ans_string(s):
    if try_this(s,'X'): return "X won"
    if try_this(s,'O'): return "O won"
    if '.' in s: return "Game has not completed"
    return "Draw"

if __name__=='__main__':
    trials=int(input())
    for i in range(trials):
        tr="Case #"+str(i+1)+": "+ans_string(make_string())
        print(tr)
