import sys

def next(n):
    ds = list(str(n))

    for i in range(len(ds)-1, -1, -1):
        less = [ds[i]<x for x in ds[i+1:]]
        if any(less):
            break
    else:
        zs = [x for x in ds if x=='0']
        nzs = sorted([x for x in ds if x!='0'])
        return ''.join([nzs[0]] + zs + ['0'] + nzs[1:])

    prefix = ds[:i]

    swapi = min( [(x+1,ds[x]) for x in range(len(less)) if less[x]] ,
            key=lambda t:t[1])
    swap = [ds[swapi[0]+i]]

    suffix = sorted(ds[i:])
    suffix.remove(swap[0])

    return ''.join(prefix+swap+suffix)

def input_line(ctors):
    return [x[0](x[1]) for x in zip(ctors,
        sys.stdin.readline().strip().split())]

if __name__ == "__main__":
    (T,) = input_line((int,))
    for case in range(1, T+1):
        (N,) = input_line((int,))
        
        print "Case #%d: %s" % (case, next(N))

