#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int T, cas; LL x, y;

void Calc(LL n, LL m) {
    if (m == 1) {
        if (n % 2 == 0) x = n / 2, y = x - 1;
        else x = y = n / 2;
        return;
    }
    if (n % 2 == 1) {
        return Calc(n / 2, m / 2);
    } else {
        if (m % 2 == 0) return Calc(n / 2, m / 2);
        else return Calc(n / 2 - 1, m / 2);
    }
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin >> T;
    while (T --) {
        LL n, m;
        scanf("%lld%lld", &n, &m);
        Calc(n, m);
        printf("Case #%d: %lld %lld\n", ++ cas, x, y);
    }
}
