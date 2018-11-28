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

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;

double f[111];
long long sd[111], d[111][111], e[111], s[111];
int n, q, u[111], v[111];

double solve() {
  f[1] = 0;

  sd[1] = 0;
  FOR (i, 2, n)
    sd[i] = sd[i - 1] + d[i - 1][i];

  FOR (i, 2, n) {
    f[i] = 1e15;
    FOR (j, 1, i)
      if (sd[i] - sd[j] <= e[j]) {
        f[i] = min(f[i], (double) (sd[i] - sd[j]) / s[j] + f[j]);
      }
  }

  return f[n];
}

int main() {
  int t;
  cin >> t;

  FOR (i, 1, t) {
    cin >> n >> q;
    FOR (i, 1, n) {
      cin >> e[i] >> s[i];
    }

    FOR (i, 1, n)
      FOR (j, 1, n)
        cin >> d[i][j];


    FOR (i, 1, q) {
      cin >> u[i] >> v[i];
    }

    double res = solve();

    cout << "Case #" << i << ": ";
    printf("%.9lf\n", res);
  }

  return 0;
}
