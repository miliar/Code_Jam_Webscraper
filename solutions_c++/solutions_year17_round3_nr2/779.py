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

#define TIME (24 * 60)

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

int f[TIME + 10][2][TIME + 10][2];
bool ok[2][TIME + 10];

int call(int cur, int start, int t0, int who) {
  int& res = f[cur][start][t0][who];

  if (res != -1) {
    return res;
  }

  if (cur == TIME) {
    //who must == start
    if (who != start || t0 != TIME / 2) {
      res = TIME;
      return res;
    }
    else {
      res = 0;
      return res;
    }
  }

  //go on with who
  res = TIME;

  if (ok[who][cur]) {
    res = min(res, call(cur + 1, start, t0 + (who == 0), who));
  }

  if (ok[1 - who][cur]) {
    res = min(res, 1 + call(cur + 1, start, t0 + ((1 - who) == 0), 1 - who));
  }

  return res;
}

int main() {
  int t;
  cin >> t;

  FOR (test, 1, t) {
    cout << "Case #" << test << ": ";

    FOR (i, 0, TIME) {
      ok[0][i] = ok[1][i] = true;
    }

    int n, m;
    cin >> n >> m;
    FOR (i, 1, n) {
      int u, v;
      cin >> u >> v;

      FOR (t, u, v - 1) {
        ok[0][t] = false;
      }
    }

    FOR (i, 1, m) {
      int u, v;
      cin >> u >> v;

      FOR (t, u, v - 1) {
        ok[1][t] = false;
      }
    }

    FOR (cur, 0, TIME)
      FOR (start, 0, 1)
        FOR (t0, 0, TIME)
          FOR (who, 0, 1) {
            f[cur][start][t0][who] = -1;
          }

    int res = TIME;
    FOR (start, 0, 1) {
        res = min(res, call(0, start, 0, start));
      }

    cout << res << endl;
  }

  return 0;
}
