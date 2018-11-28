import numeric.algorithm (sum)
for c in 1..int(read_line()) {
    [C, F, X]: read_line().split().map(float)
    n: max(0, ceil(X/C-2/F-1))
    ans: sum(k -> C/(2+k*F), 0, n-1) + X/(2+n*F)
    printf("Case #%d: %.7f\n", c, ans)
}
