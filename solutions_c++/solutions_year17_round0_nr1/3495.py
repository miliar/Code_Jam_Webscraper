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

int n, k, res, cnt_test;
string s;
void flip(int i) {s[i] = char('+' + '-' - s[i]);}

void solve() {
    cin >> s >> k;
    n = SZ(s);
    res = 0;
    rep(i, 0, n - k + 1) if(s[i] == '-') {
        rep(j, 0, k) flip(i + j);
        res ++;
    }
    rep(i, 0, n) if(s[i] == '-') res = -1;
    cout << "Case #" << ++ cnt_test << ": ";
    if(res == -1) cout << "IMPOSSIBLE\n";
    else cout << res << '\n';
}

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("test.out", "w", stdout);
    int t; cin >> t;
    while (t --) solve();
}
