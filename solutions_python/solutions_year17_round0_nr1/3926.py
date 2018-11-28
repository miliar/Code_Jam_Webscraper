def answer(s, k):
    queue = []
    already_seen = set()
    l = translate(s)
    queue.append((l, 0))
    #attempts = 0
    while len(queue) > 0:
        nq = []
        for curr, attempts in queue:
            already_seen.add(tuple(curr))
            if all(curr):
                return attempts
            else:
                all_lists = all_flips(curr, k)
                for possible in all_lists:
                    if tuple(possible) not in already_seen:
                        already_seen.add(tuple(possible))
                        nq.append((possible, attempts+1))
        queue = nq

    return -1




def all_flips(l, k):
    all_lists = []
    for i in range(len(l)- k + 1):
        if not all(l[i:k+i]):
            all_lists.append(flip_k(l, k, i))
    return all_lists

def translate(s):
    l = []
    for i in s:
        l.append(i=="+")
    return l

def turn_binary(l):
    s = ""
    for i in l:
        s+=['0','1'][i]
    return s

def flip_k(l, k, start):
    new_l = l[:]
    for i in range(k):
        new_l[start+i] = not(l[start+i])
    return new_l

def main():
    f = open("A-answer.txt", "w")
    tests = open("A-small-attempt1.in").read().splitlines()
    i = 1
    for line in tests[1:]:
        s, k = line.split()
        k = int(k)
        print(i)
        ans = answer(s,k)

        if ans == -1:
            ans = "IMPOSSIBLE"
        print(f"Case #{i}: {ans}", file=f)

        i+=1

main()
