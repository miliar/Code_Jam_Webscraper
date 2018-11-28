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
void solve(int test) {
   int d = read(), n = read(), x, y;
   int mn_s = 1, mn_m = 1000000000;
   for(int i = 1; i <= n; i ++) {
      x = read(), y = read();
      if((d - x) * mn_m > y * mn_s)
         mn_m = y, mn_s = d - x;
   }
   cout << "Case #" << test << ": ";
   printf("%.6f\n", 1. * d * mn_m / mn_s);
}
main() {
   freopen("A-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}

