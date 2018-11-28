#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; ++i)
#define frab(i, a, b) for (int i = a; i < b; ++i)
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = 2e9 + 7;
const ll MOD = 1e9 + 7;
const ll P = 29;
const ld EPS = 1e-9;
const ld PI = acos(-1);

const int N = 3e5 + 10;
const int M = 1e3 + 10;

int a[N], b[N];

ll solve() {
    int n, p;
    cin >> n >> p;
    fill(b, b + p + 2, 0);
    fr(i, n) {
        cin >> a[i];
        b[a[i] % p]++;
    }

    if (p == 2) {
        return b[0] + (b[1] + 1) / 2;
    }
    if (p == 3) {
        ll ans = b[0];
        ll t = min(b[1], b[2]);
        ans += t;
        b[1] -= t, b[2] -= t;
        ans += b[1] / 3;
        ans += b[2] / 3;
        b[1] %= 3;
        b[2] %= 3;
        if (b[1] || b[2])
            ans++;
        return ans;
    }
    if (p == 4) {
        ll ans = b[0];
        for (int t1 = 0; t1 <= min(b[1], b[3]); t1++)
            for (int t2 = 0; t2 <= b[1] / 4; t2++)
                for (int t3 = 0; t3 <= min(b[2], b[1] / 2); t3++)
                    for (int t4 = 0; t4 <= min(b[3] / 3, b[2]); t4++)
                        for (int t5 = 0; t5 <= b[2] / 2; t5++)
        for (int t6 = 0; t6 <= b[3] / 4; t6++)
            if (t1 + 4 * t2 + 2 * t3 <= b[1] && t3 + t4 + 2 * t5 <= b[2] &&
                t1 + 2 * t4 + 4 * t6 <= b[3]) {
                    ll ans2 = t1 + t2 + t3 + t4 + t5 + t6;
                    if (t1 + 4 * t2 + 2 * t3 < b[1] || t3 + t4 + 2 * t5 < b[2] ||
                t1 + 2 * t4 + 4 * t6 < b[3])
                        ans2++;
                    ans = max(ans, ans2 + b[0]);
                }
        return ans;
    }
}

int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    int tests;
    cin >> tests;
    fr(i, tests) {
        cout << "case #" << i + 1 << ": " << solve() << endl;
    }
}
