#include <bits/stdc++.h>
#define FOR(i, a, b) for (int i = a; i <= b; i ++)
using namespace std;
typedef long long ll;

ll T, N;

int isTidy(ll n) {
    ll tmp = n;
    int cnt = 0, x[123], y[123];
    while (tmp > 0) {
        x[cnt] = tmp % 10;
        y[cnt] = x[cnt];
        tmp /= 10;
        cnt ++;
    }
    sort(x, x + cnt);
    ll z[123], cntz = 0;
    for (int i = cnt - 1; i >= 0; i --)
        z[cntz ++ ] = y[i];
    for (int i = 0; i < cnt; i ++)
        if (z[i] != x[i])
            return 0;
    return 1;
}

int main() {

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%lld", &T);
    for (int c = 1; c <= T; c ++) {
        scanf("%lld", &N);
        //printf("%lld\n", N);
        for (ll i = N; i >= 1; i --)
        if (isTidy(i)) {
                cout << "Case #" << c <<": " << i << endl;
                break;
        }
    }
    return 0;

}
