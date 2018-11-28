#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define sz size
#define pb push_back
typedef long long int i64;
typedef pair<int, int> pii;
typedef pair<i64, i64> pll;

int main() {
  int t, d, n, p, s;
  double ans = 0.0, mx;
  scanf("%d", &t);
  for(int test = 1; test <= t; test++) {
    scanf("%d%d", &d, &n);
    mx = 0.0;
    for(int i = 0; i < n; i++) {
      scanf("%d%d", &p, &s);
      mx = max(mx, (d - p) * 1.0 / s);
    }
    ans = d / mx;
    printf("Case #%d: %0.6f\n", test, ans);
  }
  return 0;
}
