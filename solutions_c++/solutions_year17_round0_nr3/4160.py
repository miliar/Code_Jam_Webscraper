#include <bits/stdc++.h>

using namespace std;
using ll = long long;
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define REP(i, n)    FOR(i, 0, n - 1)

ll T, n, K;

void comp(int n, int K) {
    multiset<ll> s;
    s.insert(-n);
    REP(i, K) {
        ll D = -(*begin(s));
        s.erase(begin(s));
        ll L = (D - 1) / 2;
        ll R = (D - 1) - L;
        if (i + 1 == K) {
            cout << max(L, R) << " " << min(L, R) << "\n";
        } else {
            s.insert(-L);
            s.insert(-R);
        }
    }
}

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);

    cin >> T;
    REP(t, T) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> K;
        comp(n, K);
    }

    fclose(stdout);
}
