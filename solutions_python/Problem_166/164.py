def max_rep(target, keyboard, S):
    if S < len(target):
        return 0
        
    for l in target:
        if l not in keyboard:
            return 0

    if len(target) == 1:
        return S
            
    overlap = 0
    for i in range(1, len(target)):
        if target[:i] == target[-i:]:
            overlap = i
    if overlap == 0:
        return S // len(target)
        
    return 1 + (S-len(target))//(len(target) - overlap)



def all_strings(keyboard, S):
    if S == 1:
        return [k for k in keyboard]
    strings = all_strings(keyboard, S-1)
    to_return = []
    for s in strings:
        for k in keyboard:
            to_return.append(s + k)
    return to_return

def solve(target, keyboard, S):
    max_reps = 0
    num_reps_found = 0
    all_s = all_strings(keyboard, S)
    for s in all_s:
        reps = 0
        for i in range(S-len(target)+1):
            if s[i:i+len(target)] == target:
                num_reps_found += 1
                reps += 1
        max_reps = max(reps, max_reps)
    return max_reps - num_reps_found/float(len(all_s))

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        K, L, S = map(int, raw_input().split())
        keyboard = raw_input().strip()
        target = raw_input().strip()
        print "Case #%d: %.7f" % (i, solve(target, keyboard, S))
    
        
