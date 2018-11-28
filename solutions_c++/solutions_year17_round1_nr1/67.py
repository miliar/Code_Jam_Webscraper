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

int t, use[50][50];
string s[50];
int n, m;
void dfs(int x, int y, char c) {
   s[x][y] = c;
   use[x][y] = 1;
   //cout << x << ' ' << y << "\n";
   if (x && !use[x - 1][y] && s[x - 1][y] == '?')
      dfs(x - 1, y, c);
   if (y && !use[x][y - 1] && s[x][y - 1] == '?')
      dfs(x, y - 1, c);
   if (x + 1 < n && !use[x + 1][y] && s[x + 1][y] == '?')
      dfs(x + 1, y, c);
   if (y + 1 < m && !use[x][y + 1] && s[x][y + 1] == '?')
      dfs(x, y + 1, c);
}
void solve() {
   
   cin >> n >> m;
   forn (i, n) {
      cin >> s[i];
      forn (j, m) use[i][j] = 0;
   }
   forn (i, n) {

      forn (j, m) {
         if (s[i][j] == '?') {
            if (j) s[i][j] = s[i][j - 1];
            //dfs(i, j, s[i][j]);
         }
      }
      for (int j = m - 2; j >= 0; j--) {
         if (s[i][j] == '?') s[i][j] = s[i][j + 1];
      }
      bool ok = false;
      forn (j, m)
         if ( s[i][j] != '?') ok = true;
      if (!ok && i) s[i] = s[i - 1];
   }
   for (int i = n - 2; i >= 0; i--) {
      bool ok = false;
      forn (j, m)
         if ( s[i][j] != '?') ok = true;
      if (!ok) s[i] = s[i + 1];  
   }
   forn (i, n) {
      cout << s[i] << "\n";
   }
}
int main() {
   iostream::sync_with_stdio(0);
   freopen("a.in", "r", stdin);
   freopen("a.out", "w", stdout);
   cin >> t;
   forn (i, t) {
      cout << "Case #" << i + 1 << ":\n";
      solve();
   }   
}

