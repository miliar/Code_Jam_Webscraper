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

double p[100];

int main() {
  int ntest;
  cin >> ntest;
  FOR (test, 1, ntest) {
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;

    FOR (i, 1, n) {
      cin >> p[i];
    }

    double low = 0, high = 1;
    FOR (i, 1, 100) {
      double mid = (low + high) / 2;
      double need = 0;
      FOR (i, 1, n) if (mid > p[i]) need += mid - p[i];
      if (need <= u) {
        low = mid;
      } else {
        high = mid;
      }
    }

    double res = 1;
    FOR (i, 1, n) res *= max(low, p[i]);
    printf("Case #%d: %.10lf\n", test, res);
  }
}

