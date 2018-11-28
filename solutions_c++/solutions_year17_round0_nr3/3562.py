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

int n, k, x, y, cnt_test;
set<int> S;
set<ii> pq;

void solve() {
    S.clear();
    pq.clear();
    cin >> n >> k;
    S.insert(0);
    S.insert(n + 1);
    pq.insert(ii(-n - 1, 0));
    while (k --) {
        ii tmp = *pq.begin(); pq.erase(pq.begin());
        int len = -tmp.fi, L = tmp.se, R = L + len, mid = L + len / 2;
        pq.insert(ii(L - mid, L));
        pq.insert(ii(mid - R, mid));
        x = mid - L - 1;
        y = R - mid - 1;
    }
    cout << "Case #" << ++ cnt_test << ": ";
    cout << max(x, y) << ' ' << min(x, y) << '\n';
}

int main() {
//    //freopen("test.txt", "r", stdin);
//    freopen("C-small-2-attempt0.in", "r", stdin);
//    freopen("test.out", "w", stdout);
    int t; cin >> t;
    while (t --) solve();
}
