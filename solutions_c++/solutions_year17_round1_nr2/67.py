#include <bits/stdc++.h>
  
using namespace std;
#define forn(i, n) for (int i = 0; i < n; i++)
#define re return
#define fi first
#define mp make_pair
#define se second
#define sz(a) (int)a.size()
#define prev previ
#define tm tmmm
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;

vector<ll> c;
vector<pair<int, int> > pq[10000];
void solve() {
   int n, p;
   cin >> n >> p;
   int ans = 0;
   c.resize(n);
   forn (i, n) {
      cin >> c[i];
   }
   ll ma = 1000000;
   forn (i, n) {
      pq[i].resize(0);
      ll ma1 = 0;
      forn (j, p) {
         ll k;
         cin >> k;
         ll r = (k *100LL) / (c[i] * 90LL), 
            l = (k * 100LL + c[i] * 110LL - 1LL) / (c[i] * 110LL);
         if (l <= r) pq[i].push_back(mp(l, r)); 
         ma1 = max(ma1, r);
      }
      ma = min(ma1, ma);
      sort(pq[i].begin(), pq[i].end());
   }
   for (int k = ma; k >= 1; k--) {
      int ok = 2;
      ans--;
      while (ok == 2) {
         ans++;
         forn (i, n) {
            while (sz(pq[i]) && pq[i][sz(pq[i]) - 1].fi > k) pq[i].pop_back();
            if (sz(pq[i]) == 0) {
               ok = 0;
               break;
            } 
            if (pq[i][sz(pq[i]) - 1].se < k) {
               ok = 1;
               break;
            }
         }
         if (ok == 2) {
            forn (i, n) pq[i].pop_back();
         }
      }
      if (ok == 0) break;
      forn (i, n) {
         k = min(k, pq[i][sz(pq[i]) - 1].se + 1);
      }
   }
   cout << ans << "\n";
}
int main() {
   iostream::sync_with_stdio(0);
   freopen("a.in", "r", stdin);
   freopen("a.out", "w", stdout);
   int t;
   cin >> t;
   forn (i, t) {
      cout << "Case #" << i + 1 << ": ";
      solve();
   }   
}

