import algebra::euclid (gcd)

solve(P, Q) := {
    # Check whether Q=2^m
    q := Q
    while (q != 1) {
        if q % 2 == 1
            return "impossible"
        q //= 2
    }
    ans := 1
    while (2*P < Q) {
        Q //= 2
        ans += 1
    }
    return ans
}

for c in 1..int(read_line()) {
    [P, Q] := read_line().split("/").map(int)
    g := gcd(P, Q)
    puts (P, Q)
    puts g
    printf "Case #%d: %s\n", c, solve(P//g, Q//g)
}
