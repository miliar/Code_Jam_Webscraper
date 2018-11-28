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
typedef long double ld;
typedef pair<int, int> ii;
const int mod = (int) 1e9 + 7;
const int maxn = (int) 2e5 + 5;
const double eps = 1e-9;

int cnt_test;
int n, p, a[4], sum;
void solve() {
    rep(i, 0, 4) a[i] = 0;
    sum = 0;
    cin >> n >> p;
    rep(i, 0, n) {
        int x; cin >> x;
        a[x % p] ++;
        sum += (x % p);
    }
    if(p == 2) a[0] += a[1] / 2;
    if(p == 3) {
        int x = min(a[1], a[2]);
        a[1] -= x, a[2] -= x;
        a[0] += x;
        a[0] += a[1] / 3 + a[2] / 3;
    }
    if(p == 4) {
        int x = min(a[3], a[1]);
        a[3] -= x, a[1] -= x;
        a[0] += x + (a[3] / 4);
        a[0] += a[2] / 2;
        if(a[1] > 1 && (a[2] & 1)) a[1] -= 2, a[0] ++;
        a[0] += a[1] / 4;
    }
    if(sum % p != 0) a[0] ++;
    cout << "Case #" << ++ cnt_test << ": " << a[0] << '\n';
}

int main() {
    freopen("test.txt", "r", stdin);
    freopen("test.out", "w", stdout);
    int t; cin >> t;
    while (t --) solve();
}
