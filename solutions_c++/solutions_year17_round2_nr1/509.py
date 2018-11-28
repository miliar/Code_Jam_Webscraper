#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
const int mod = (int) 1e9 + 7;
const int maxn = (int) 2e5 + 5;
const double eps = 1e-9;

int n, d, cnt_test;
ll k[maxn], s[maxn];

bool check(ld x) {
    rep(i, 1, n + 1) {
        if(x * (d - k[i]) > 1.0 * d * s[i]) return 0;
    }
    return 1;
}

void solve() {
    cin >> d >> n;
    double res = 1e18;
    rep(i, 1, n + 1) {
        cin >> k[i] >> s[i];
        res = min(res, 1.0 * d * s[i] / (d - k[i]));
    }
    cout << "Case #" << ++ cnt_test << ": ";
    cout << fixed << setprecision(6) << res << endl;
}

int main() {
//    freopen("test.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    ios_base::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t --) solve();
}

