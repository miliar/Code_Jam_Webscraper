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
   int hd, ad, hk, ak, b, d;
   cin >> hd >> ad >> hk >> ak >> d >> b;
   int ans = int(1e9);
   for (int cb = 0; cb <= 100; cb++) {
      for (int cd = 0; cd <= 100; cd++) {
         ad += d * cd;
         int at = (hk + ad - 1) / ad;
         //cout << cb << " " << cd << " " << at << "\n";
         int ns = 0;
         int weh = hd, akk = ak;
         bool ok = true;
         forn (i, cb) {
            ns++;
            if (weh - akk + min(akk, b) <= 0) {
               ns++;
               weh = hd;
               weh -= akk;
               if (weh - akk + min(akk, b) <= 0) {
                  ok = false;
                  break;
               }
            }
            akk -= min(akk, b);
            weh -= akk;
         }
         forn (i, cd) {
            ns++;
            if (weh - akk <= 0) {
               ns++;
               weh = hd - akk;
               if (weh - akk <= 0) {
                  ok = false;
               }
            }
            weh -= akk;
         }
         forn (i, at) {
            ns++;
            if (weh - akk <= 0 && i + 1 < at) {
               ns++;
               weh = hd - akk;
               if (weh - akk <= 0) {
                  ok = false;
               }
            }
            weh -= akk;
         }
         if (ok) {
            ans = min(ans, ns);
            //cout << ns << "\n";
         }
         ad -= d * cd;
      }
   } 
   if (ans == int(1e9)) 
      cout << "IMPOSSIBLE\n";
   else
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

