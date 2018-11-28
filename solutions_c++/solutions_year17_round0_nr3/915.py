#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    ll n, k, x, y;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%lld %lld", &n, &k);

        while(1) {
            x = y = (n-1)/2;
            if (n%2 == 0) x++;

            if (k == 1) break;

            if (k&1) n = y;
            else n=x;

            k /= 2;
        }

        printf("Case #%d: %lld %lld\n", ncase, x, y);
    }

    return 0;
}
