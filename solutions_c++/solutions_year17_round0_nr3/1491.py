
#include <bits/stdc++.h>
  
using namespace std;
#define forn(i, n) for (int i = 0; i < n; i++)
#define re return
#define fi first
#define mp make_pair
#define se second
#define sz(a) (int)a.size()
#define tm tmmm
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const ll mod = ll(1e9) + 7, p = 239;
const int ma = 16 * 1024;

int t;

int main() {
   iostream::sync_with_stdio(0);
   //freopen("a.in", "r", stdin);
   //freopen("a.out", "w", stdout);
   cin >> t;
   forn (i, t) {
      ll n, k;
      cin >> n >> k;
      vector<pair<ll, ll> > a[64];
      a[0].push_back(mp(n, 1));
      forn (i, 61) {
         forn (jj, sz(a[i])) {
            ll a1 = (a[i][jj].fi  - 1LL) / 2LL, a2 = a[i][jj].fi - 1LL - (a[i][jj].fi  - 1LL) / 2LL;
            if (sz(a[i + 1]) && a[i + 1][sz(a[i + 1]) - 1].fi == a1)
               a[i + 1][sz(a[i + 1]) - 1].se += a[i][jj].se;
            else
               a[i + 1].push_back(mp(a1, a[i][jj].se));
            if (sz(a[i + 1]) && a[i + 1][sz(a[i + 1]) - 1].fi == a2)
               a[i + 1][sz(a[i + 1]) - 1].se += a[i][jj].se;
            else
               a[i + 1].push_back(mp(a2, a[i][jj].se));
         }
      }  
      ll l = -1, r = -1;
      forn (i, 61) {
         for (int jj = sz(a[i]) - 1; jj >= 0; jj--) {
            if (a[i][jj].se >= k) {
               l = (a[i][jj].fi - 1LL) / 2LL, r = a[i][jj].fi - 1LL - (a[i][jj].fi - 1LL) / 2LL;
               break;
            }
            k -= a[i][jj].se;
         }
         if (l != -1) break;
      }
      cout << "Case #" << i + 1 << ": " << r << " " << l << "\n";
   } 
}
