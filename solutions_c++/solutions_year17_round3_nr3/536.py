#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

const double esp = 1e-6;

double a[100];
int T, n, m;
double u, res, diff, sum;

int main() {
  freopen("C1.in", "r", stdin);
  freopen("C1.out", "w", stdout);
  cin >> T;
  rep(cas, 1, T + 1) {
    cin >> n >> m;
    cin >> u;
    sum = 0;
    rep(i, 0, n) {
      cin >> a[i];
      sum += a[i];
    }
    if (sum + u + esp > n) {
      cout << "Case #" << cas << ": 1.000000" << endl;
      continue;
    }
    sort(a, a + n);
    a[n] = 1;
    int count;
    while (u > esp) {
      count = 1;
      diff = 0;
      rep(i, 1, n + 1)
        if (fabs(a[i] - a[i - 1]) < esp)
          count ++;
        else {
          diff = a[i] - a[i - 1];
          break;
        }
      if (diff * count > u) {
        diff = u / count;
        u = 0;
      } else {
        u -= diff * count;
      }
      rep(i, 0, count)
        a[i] += diff;
    }
    res = 1;
    rep(i, 0, n)
      res *= a[i];
    printf("Case #%d: %.6lf\n", cas, res);
  }
  return 0;
}
