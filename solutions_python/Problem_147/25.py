import math (sqrt)

solve(N, M, K) := {
    mink := infinity
    # brute force
    for n in 3..N {
        for m in 3..M {
            for a in 1..n-2 {
                for b in 1..n-a-1 {
                    for c in 1..m-a-1 {
                        for d in 1..min(n-c-1,m-b-1) {
                            k := 2*m + 2*n - a - b - c - d - 4
                            r := K -(m*n - a*(a+1)//2 - b*(b+1)//2 - c*(c+1)//2 - d*(d+1)//2)
                            k += r if r > 0
                            mink = k if k < mink
                        }
                    }
                }
            }
        }
    }
    return mink
}
solve(N, M, K) when N <= 2 or M <= 2 or K <= 4 := K

for c in 1..int(read_line()) {
    [N, M, K] := read_line().split().map(int)
    printf "Case #%d: %d\n", c, solve(N, M, K)
}
