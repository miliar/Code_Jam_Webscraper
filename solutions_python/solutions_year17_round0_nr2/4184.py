def issorted(S):
    return all(S[i] <= S[i+1] for i in range(len(S)-1))

T = int(raw_input())
for i in range(T):
    a = raw_input()
    b = a
    while int(b) != int(a)/2:
        if issorted(b):
            print("Case #" + str(i+1) + ": " + b)
            break
        else:
            if len(b) > 10 and list(b)[len(b)-1] == '0':
                c = ''.join(list(b)[:len(b)-1])
                b = str(int(b) - int(c))
            else:
                b = str(int(b) - 1)
