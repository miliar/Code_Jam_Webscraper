#include <bits/stdc++.h>

#define pb push_back
#define db double
#define pi acos(-1)
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
struct pt {
   int r, h, v;
};
bool comp(pt a, pt b) {
   return a.r > b.r || (a.r == b.r && a.v > b.v);
}
pt a[N];
int dp[1001][3];
void solve(int test) {
   int n = read(), k = read();
   for(int i = 1; i <= n; i ++) {
      a[i].r = read(), a[i].h = read();
      a[i].v = a[i].r * a[i].h;
   }
   sort(a + 1, a + n + 1, comp);
   priority_queue <int> q;
   int sum = 0, ans = 0;
   for(int i = n; i >= 1; i --) {
      if(q.size() < k - 1) {
         sum += a[i].v;
         q.push(-a[i].v);
      }
      else {
         ans = max(ans, a[i].r * a[i].r + 2 * (a[i].v + sum));
         if(q.size() && a[i].v > -q.top()) {
            sum += q.top();
            sum += a[i].v;
            q.pop();
            q.push(-a[i].v);
         }
      }
   }
   cout << "Case #" << test << ": ";
   printf("%.9f\n", ans * pi);
}
main() {
   freopen("A-large.in", "r", stdin);
//   freopen("A-small-attempt0.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}

