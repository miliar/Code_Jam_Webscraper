#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int _ = 1; _ <= test; _++) {
        long long x, K;
        cin >> x >> K;

        long long KK = K;
        long long i = 0;
        long long aa = 1;
        for(; (aa << i) < K; i++) {
            K -= (1LL << i);
        }
        x -= (KK - K);
        long long y = x / (aa << i) + (K <= (x % (aa << i)));
        printf("Case #%d: %I64d %I64d\n", _, y / 2, (y - 1) / 2);
    }
    return 0;
}
