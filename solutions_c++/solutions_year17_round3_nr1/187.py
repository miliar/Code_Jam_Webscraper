#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define PB push_back
#define MP make_pair

#define radius first
#define height second

const double pi = acos(-1);

double surround(pii a) {
  return 2 * pi * a.radius * a.height;
}

double surface(pii a) {
  return pi * a.radius * a.radius;
}

#define MAX 1011
double f[MAX][MAX];

int main() {
  int ntest;
  cin >> ntest;

  FOR (test, 1, ntest) {
    cerr << test << endl;
    cout << "Case #" << test << ": ";

    int n, choose;
    cin >> n >> choose;

    pii a[n + 1];
    FOR (i, 1, n) cin >> a[i].first >> a[i].second;
    sort(a + 1, a + n + 1);

    FOR (i, 1, n) FOR (j, 1, choose) f[i][j] = 0;

    double res = 0;
    FOR (i, 1, n) {
      f[i][1] = surround(a[i]) + surface(a[i]);

      FOR (j, 2, min(i, choose)) {
        FOR (k, j - 1, i - 1) {
          f[i][j] = max(f[i][j], f[k][j - 1] + surround(a[i]) + surface(a[i]) - surface(a[k]));
        }
      }

      res = max(res, f[i][choose]);
    }

    printf("%.10lf\n", res);
  }
}

