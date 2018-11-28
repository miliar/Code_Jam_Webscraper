#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

pair<long long, long long> get_res(long long n) {
    if(n % 2 == 0) {
        return pair<long long, long long>(n / 2, n / 2 - 1);
    }

    return pair<long long, long long>(n / 2, n / 2);
}

void solve1(long long n, long long rem, long long a, long long b) {
    // printf("n = %lld, rem = %lld, a = %lld, b = %lld\n", n, rem, a, b);
    if(a + b >= rem) {
        pair<long long, long long> res;
        if(b >= rem) {
            res = get_res(n + 1);
        } else {
            res = get_res(n);
        }
        printf("%lld %lld\n", res.first, res.second);
        return;
    }

    long long new_n;
    long long new_a, new_b;
    if(n % 2 == 0) {
        new_n = n / 2 - 1;
        new_a = a;
        new_b = a + 2 * b;
    } else {
        new_n = n / 2;
        new_a = 2 * a + b;
        new_b = b;
    }

    solve1(new_n, rem - a - b, new_a, new_b);
}

void solve() {
    long long N, K;
    scanf("%lld %lld", &N, &K);
    solve1(N, K, 1, 0);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
