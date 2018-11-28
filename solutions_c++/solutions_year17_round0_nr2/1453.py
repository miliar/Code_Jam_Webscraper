
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
      string s;
      cin >> s;
      bool ok = true;
      forn (i, sz(s)) {
         if (s[i] < '1') {
            ok = false;
            break;
         }
         if (s[i] > '1') {
            break;
         }
      }
      cout << "Case #" << i + 1 << ": ";
      if (!ok) {
         forn (i, sz(s) - 1)
            cout << "9";
         cout << "\n";
         continue;
      }
      string ans = "";
      forn (i, sz(s)) {
         bool ok = true;
         for (int j = i + 1; j < sz(s); j++) {
            if (s[j] < s[i]) {
               ok = false;
               break;
            }
            if(s[j] > s[i])
               break;
         }
         if (ok) {
            ans += s[i];
            continue;
         }
         ans += char(s[i] - 1);
         while (sz(ans) < sz(s)) ans += "9";
         break;
      }
      cout << ans << '\n';
   } 
}

