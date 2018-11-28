#include <bits/stdc++.h>

using namespace  std;

using ll = long long;

#define clr(a) (a.clear())
#define MP(a,b) make_pair(a,b)
#define sz(x) (int)x.size()
#define mem(a,b) memset(a, b, sizeof(a))
#define Unique(store) store.resize(unique(store.begin(),store.end())-store.begin())
#define pb push_back
#define FAST ios_base::sync_with_stdio(0);cin.tie(0);

#define X first
#define Y second

using pii = pair <int , int>;
using pll = pair <ll , ll>;
const ll inf = 1;
const ll mod = 1E9;

#define SZ 100010


int main() {
//    #if defined JESI
//        freopen("C-small-attempt0.in", "r", stdin);
//        freopen("2.txt", "w", stdout);
//    #endif

    ios::sync_with_stdio(false);

    int t;
    cin >> t;

    for (int cs = 0; cs < t; cs++) {
        int n, q;
        cin >> n >> q;
        vector <pii> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i].X >> a[i].Y;
        }
        vector <int> dist(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i + 1 == j) {
                    cin >> dist[i];
                } else {
                    int x;
                    cin >> x;
                }
            }
        }
        int p, qq;
        cin >> p >> qq;
        vector <double> ans(n, 1E16);
        ans[0] = 0;
        for (int i = 0; i < n - 1; i++) {
            ll tot = 0;
            for (int j = i; j < n - 1; j++) {
                tot += (ll)dist[j];
                if (tot <= a[i].X) {
                    ans[j + 1] = min(ans[j + 1], ans[i] + (double)tot / (double)a[i].Y);
                } else {
                    break;
                }
            }
        }
        cout << fixed << setprecision(10) << "Case #" << cs + 1 << ": " << ans[n - 1] << endl;
    }

    return 0;
}






