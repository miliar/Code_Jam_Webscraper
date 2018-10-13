file=open('input.txt','rt')
out_file = open('output.txt','wt')

test_cases = file.readline()

def imul(l):
    res = 1

    for x in l:
        res*=x
    return res

def e_finish(typed_chars, prob_chars, pass_chars):
    correct = imul(prob_chars)
    correct_len = pass_chars-typed_chars + 1
    wrong = 1-correct
    wrong_len = correct_len + pass_chars + 1

    return correct*correct_len+wrong*wrong_len

def e_enter(typed_chars, prob_chars, pass_chars):
    return 1 + pass_chars + 1

def e_backspace(typed_chars, prob_chars, pass_chars, back_chars):
    typed_chars -= back_chars
    prob_chars = prob_chars[0:typed_chars]

    correct = imul(prob_chars)
    correct_len = back_chars + (pass_chars - typed_chars) + 1
    wrong = 1 - correct
    wrong_len = correct_len + pass_chars + 1
    return correct*correct_len+wrong*wrong_len

for i in range(int(test_cases)):
    typed_chars, pass_chars = file.readline().split(' ')
    typed_chars = int(typed_chars)
    pass_chars = int(pass_chars)
    prob_chars = [float(x) for x in file.readline().split(' ')]

    ee = e_enter(typed_chars, prob_chars, pass_chars)
    ef = e_finish(typed_chars, prob_chars, pass_chars)

    print(typed_chars, prob_chars, pass_chars, ee)
    print(typed_chars, prob_chars, pass_chars, ef)
    m = min(ee, ef)
    for back_chars in range(1,typed_chars+1):
        be = e_backspace(typed_chars, prob_chars, pass_chars, back_chars)
        m = min(be, m)
        print(typed_chars, prob_chars, pass_chars, back_chars, be)

    outtext = 'Case #{0}: {1:.6f}'.format((i+1),m)
    out_file.write(outtext+'\n')
    print(outtext)

out_file.flush()
out_file.close()