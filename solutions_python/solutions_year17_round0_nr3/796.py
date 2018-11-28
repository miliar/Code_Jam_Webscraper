import sys

def res(P):
    if P%2==0:
        return (P/2),P/2-1
    else:
        return ((P-1)/2),((P-1)/2)

def solve(N,K):
    empty_spaces = {N:1} #(Max,Min):Number

    k=0
    while k < K:
        keys = empty_spaces.keys()
        keys.sort(reverse=True)

        if empty_spaces[keys[0]]>=K-k:
            #Fin
            return res(keys[0])

        else:
            removed_number = empty_spaces.pop(keys[0])
            k += removed_number

            new_holes = res(keys[0])
            for i in [0,1]:
                if new_holes[i] in empty_spaces:
                    empty_spaces[new_holes[i]]+=removed_number
                else :
                    empty_spaces[new_holes[i]]=removed_number


    return '!'


if __name__ == '__main__':
    in_path = sys.argv[1]
    out_path = sys.argv[2]

    with open(in_path, "r") as f:
        N = int(f.readline())

        out = open(out_path, 'w')

        for i in range(N):
            out.write('Case #' + (str(i + 1)) + ": ")
            new = f.readline().split(" ")

            N = int(new[0])
            K = int(new[1])
            t = solve(N,K)
            print(solve(N,K))

            out.write(str(t[0])+" "+str(t[1]))
            out.write('\n')

        out.close()