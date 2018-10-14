import sys
sys.setrecursionlimit(5000)

def pancake_flipper_solve(S, K, past_flips):
    if len(S) == K:
        if S == '-' * K:
            return 1 + past_flips
        elif S == '+' * K:
            return past_flips
        else:
            return "IMPOSSIBLE"
    if S[0] == '+':
        return pancake_flipper_solve(S[1:], K, past_flips)
    else:
        adjustedS = ''
        for i in range(1, len(S)):
            if i < K:
                if S[i] == '-':
                    adjustedS += '+'
                else:
                    adjustedS += '-'
            else:
                adjustedS += S[i]
        return pancake_flipper_solve(adjustedS, K, past_flips + 1)
         
def pancake_flipper_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    for i in range(1, T + 1):
        inputs = f.readline().split()
        S = inputs[0]
        K = int(inputs[1])
        flip_count = pancake_flipper_solve(S, K, 0)
        
        output_f.write("Case #" + str(i) + ": " + str(flip_count) + "\n")
    return 1

pancake_flipper_main("A-large.in", "A-large.out")
