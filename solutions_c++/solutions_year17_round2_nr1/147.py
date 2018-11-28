#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; i++)
#define frab(i, a, b) for (int i = a; i < b; i++)
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = 2e15 + 10;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int N = 5e5 + 10;
const int M = 1e3 + 10;

ll k[N], s[N];

ld solve() {
    ll d, n;
    cin >> d >> n;
    fr(i, n)
        cin >> k[i] >> s[i];
    ld l = 0, r = INF;
    fr(i1, 100) {
        bool ok = true;
        ld m = (l + r) / 2;
        for (int i = 0; i < n && ok; i++)
            if (d * s[i] < m * (d - k[i]))
                ok = false;
        if (ok)
            l = m;
        else
            r = m;
    }
    return l;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    fr(i, t) {
        cout << "Case #" << i + 1 << ": ";
        cout << fixed << setprecision(12) << solve() << endl;
    }
}
