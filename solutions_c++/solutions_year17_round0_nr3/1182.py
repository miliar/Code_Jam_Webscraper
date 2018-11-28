#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; i++)
#define frab(i, a, b) for (int i = a; i < b; i++)
#define mp make_pair

using namespace std;

typedef long long ll;

pair <ll, ll> solve(ll n, ll k) {
    ll t1 = n;
    ll q1 = 1, q2 = 0;
    while (true) {
        if (k <= q2) {
            return mp((t1 + 1) / 2, t1 / 2);
        }
        else if (k <= q1 + q2) {
            return mp(t1 / 2, (t1 - 1) / 2);
        }
        k -= (q1 + q2);
        ll copt1 = t1, copq1 = q1, copq2 = q2;
        t1 = (copt1 - 1) / 2;
        if (copt1 % 2 == 0) {
            q1 = copq1;
            q2 = 2 * copq2 + copq1;
        }
        else {
            q1 = 2 * copq1 + copq2;
            q2 = copq2;
        }
    }
}

int main() {
    //srand(time(NULL));
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    int tests;
    cin >> tests;
    fr(i, tests) {
        ll n, k;
        cin >> n >> k;
        auto ans = solve(n, k);
        cout << "Case #" << i + 1 << ": " << ans.first << " " << ans.second << endl;
    }
}
