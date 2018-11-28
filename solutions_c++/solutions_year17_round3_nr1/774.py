#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define SQR(x) ((x) * (x))
#define PI (acos(-1))

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

int n, k;
pll c[1111];
double f[1111][1111];

int main() {
  int t;
  cin >> t;

  FOR (test, 1, t) {
    cout << "Case #" << test << ": ";

    cin >> n >> k;
    FOR (i, 1, n) {
      cin >> c[i].first >> c[i].second;
    }

    double res = 0;
    sort(c + 1, c + 1 + n);

    FOR(i, 1, n) {
      long long r = c[i].first, h = c[i].second;
      f[i][1] = r * 2 * PI * h + r * r * PI;

      FOR (j, 2, min(i, k)) {
        f[i][j] = -1;
        FOR (e, j - 1, i - 1) {
          f[i][j] = max(f[i][j], r * 2 * PI * h + r * r * PI + f[e][j - 1] - SQR(c[e].first) * PI);
        }
      }

      if (i >= k) {
        res = max(res, f[i][k]);
      }
    }

    printf("%.9lf\n", res);
  }

  return 0;
}
