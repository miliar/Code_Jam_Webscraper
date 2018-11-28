#include <bits/stdc++.h>

#define pb push_back
#define db double
#define int long long
#define all(c) (c).begin(), (c).end()
using namespace std;

const int N = 1e5 + 1;
const int mod = 1e9 + 7;
typedef pair<int, int> pii;

inline int read () {
   char c = getchar();
   int t = 0, f = 1;
   while (!isdigit(c)) f = (c == '-') ? -1 : 1, c = getchar();
   while (isdigit(c)) t = t * 10 + c - 48, c = getchar();
   return t * f;
}
int x[N], y[N], p[N], s[N];
double dp[N];
void solve(int test) {
   cout << "Case #" << test << ": ";
   int n = read(), q = read();
   for(int i = 1; i <= n; i ++) {
      x[i] = read();
      y[i] = read();
   }
   int l;
   for(int i = 1; i <= n; i ++) {
      for(int j = 1; j <= n; j ++) {
         l = read();
         if(i + 1 == j)
            p[i] = l;
      }
   }
   l = read();
   l = read();
   int sum = 0;
   for(int i = 1; i < n; i ++) {
      sum += p[i];
      s[i + 1] = sum;
   }
   for(int i = 1; i <= n; i ++)
      dp[i] = 1e15;
   dp[1] = 0;
   for(int i = 2; i <= n; i ++) {
      for(int j = i - 1; j >= 1; j --) {
         if(s[i] - s[j] <= x[j]) {
            dp[i] = min(dp[i], dp[j] + 1. * (s[i] - s[j]) / y[j]);
         }
      }
   }
   printf("%.6f\n", dp[n]);
}
main() {
   freopen("C-small-attempt1.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}

