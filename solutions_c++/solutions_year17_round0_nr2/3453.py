#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef long long ll;
typedef pair<int,int> ii;
const int mod = (int) 1e9 + 7;

int n, cnt_test;
string s;
ll memo[20][2][10], pw[20];

ll f(int pos, int x, int digit) {
    if(pos == n) return 0;
    ll &res = memo[pos][x][digit];
    if(res != -1) return res;
    int hi = (x ? s[pos] - '0' : 9);
    rep(i, digit, hi + 1) {
        bool y = (x && (i == s[pos] - '0'));
        if(f(pos + 1, y, i) != -1) res = max(res, pw[n - 1 - pos] * i + f(pos + 1, y, i));
    }
    return res;
}

void solve() {
    memset(memo, -1, sizeof memo);
    cin >> s;
    n = SZ(s);
    cout << "Case #" << ++ cnt_test << ": ";
    cout << f(0, 1, 0) << '\n';
}

int main() {
    //freopen("test.txt", "r", stdin);
//    freopen("B-large.in", "r", stdin);
//    freopen("test.out", "w", stdout);
    pw[0] = 1;
    rep(i, 1, 20) pw[i] = pw[i - 1] * 10;
    int t; cin >> t;
    while (t --) solve();
}
