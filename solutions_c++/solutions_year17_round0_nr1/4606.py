#include <bits/stdc++.h>

#define pb push_back
#define db double
#define int long long
#define all(c) (c).begin(), (c).end()
using namespace std;

const int N = 1e6 + 1;
const int mod = 1e9 + 7;
typedef pair<int, int> pii;

inline int read () {
   char c = getchar();
   int t = 0, f = 1;
   while (!isdigit(c)) f = (c == '-') ? -1 : 1, c = getchar();
   while (isdigit(c)) t = t * 10 + c - 48, c = getchar();
   return t * f;
}
int t[10001], n;
void inc(int i, int delta) {
   for(; i <= n; i = (i | (i + 1)))
      t[i] += delta;
}
int sum(int i) {
   int res = 0;
   for(; i > 0; i = (i & (i + 1)) - 1)
      res += t[i];
   return res;
}
void solve(int test) {
   string s;
   int k;
   cin >> s >> k;
   n = s.size();
   s = "@" + s;
   bool yes = 1;
   for(int i = 1; i <= n; i ++) {
      if(s[i] == '-') {
         inc(i, 1);
         yes = 0;
         inc(i + 1, -1);
      }
   }
   int ans = 1000000;
   for(int it = 1; it <= n - k + 1; it ++) {
      for(int i = 0; i <= 1000; i ++)
         t[i] = 0;
      for(int i = 1; i <= n; i ++) {
         if(s[i] == '-') {
            inc(i, 1);
            inc(i + 1, -1);
         }
      }
      int l = it, r = it + k - 1, cur, res = 0;
      for(int i = 1; i < l; i ++) {
         cur = sum(i);
         if(cur & 1) {
            res ++;
            inc(i, 1);
            inc(i + k, -1);
         }
      }
      for(int i = n; i > r; i --) {
         cur = sum(i);
         if(cur & 1) {
            res ++;
            inc(i - k + 1, 1);
         }
      }
      bool ok = true;
      for(int i = l; i <= r; i ++)
         if(!(sum(i) & 1))
            ok = false;
      if(ok) {
         ans = min(ans, res + 1);
      }
   }
   if(yes) {
         cout << "Case #" << test << ": 0" << endl;
   }
   else {
      if(ans == 1000000)
         cout << "Case #" << test << ": IMPOSSIBLE" << endl;
      else
         cout << "Case #" << test << ": " << ans << endl;
   }
}
main() {
   freopen("A-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}
/**
10
+-++--+-+ 3
--+- 2
*/
