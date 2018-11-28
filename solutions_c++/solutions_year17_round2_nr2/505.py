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

int a[6], r, y, b, cnt_test, n;

string calc(int r, int y, int b) {
    string t = "RYB";
    vector<int> c, ans;
    //cout << r << ' ' << y << ' ' << b <<endl;
    c.pb(r);
    c.pb(y);
    c.pb(b);
    int f = 0;
    rep(i, 0, 3) {
        if(c[i] > 0) {
            f = i;
            ans.pb(i);
            c[i] --;
            break;
        }
    }
    //cout << ans[0] << endl;
    rep(t, 1, r + y + b) {
        int p = -1, mx = 0;
        rep(i, 0, 3) if(c[i] > 0 && i != ans.back()) {
            if (c[i] > mx) mx = c[i], p = i;
            else if(c[i] == mx) {
                if(i == ans[0]) p = i;
            }
        }
        if(p == -1) return "";
        ans.pb(p);
        c[p] --;
        if(ans.size() == r + y + b && ans.back() == ans[0]) return "";
    }
    string s = "";
    rep(i, 0, SZ(ans)) {
        s += t[ans[i]];
    //    cout << ans[i];
    }
    return s;
}

void solve() {
    cin >> n;
    cin >> a[0] >> a[5] >> a[1] >> a[3] >> a[2] >> a[4];
    cout << "Case #" << ++ cnt_test << ": ";

    if(a[0] == a[3] && a[0] + a[3] == n) {
        rep(i, 0, n) {
            if(i & 1) cout << 'R';
            else cout << 'G';
        }
        cout << endl;
        return;
    }
    if(a[1] == a[4] && a[1] + a[4] == n) {
        rep(i, 0, n) {
            if(i & 1) cout << 'Y';
            else cout << 'V';
        }
        cout << endl;
        return ;
    }
    if(a[2] == a[5] && a[2] + a[5] == n) {
        rep(i, 0, n) {
            if(i & 1) cout << 'B';
            else cout << 'O';
        }
        cout << endl;
        return ;
    }
    r = a[0], y = a[1], b = a[2];
    if(a[3] > 0 && r <= a[3]) return cout << "IMPOSSIBLE\n", void();
    else r -= a[3];
    if(a[4] > 0 && y <= a[4]) return cout << "IMPOSSIBLE\n", void();
    else y -= a[4];
    if(a[5] > 0 && b <= a[5]) return cout << "IMPOSSIBLE\n", void();
    else b -= a[5];
    string s = calc(r, y, b);
    //return ;
    if(s == "") return cout << "IMPOSSIBLE\n", void();
    string res = "";
    int _r = 0, _y = 0, _b = 0;
    rep(i, 0, SZ(s)) {
        res += s[i];
        if(s[i] == 'R' && !_r) {
            _r = 1;
            rep(j, 0, a[3]) res += "GR";
        }
        if(s[i] == 'Y' && !_y) {
            _y = 1;
            rep(j, 0, a[4]) res += "VY";
        }
        if(s[i] == 'B' && !_b) {
            _b = 1;
            rep(j, 0, a[5]) res += "OB";
        }
    }
    cout << res << endl;
}

int main() {
//    freopen("test.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    ios_base::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t --) solve();
}

