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

int n;
double d;
double k[1111], s[1111];

int main() {
  int t;
  cin >> t;

  FOR (i, 1, t) {
    cin >> d >> n;

    FOR (i, 1, n) {
      cin >> k[i] >> s[i];
    }

    double maxt = (d - k[1]) / s[1];
    double a = (d - k[1]);
    double b = s[1];

    FOR (i, 1, n) {
      maxt = max(maxt, (d - k[i]) / s[i]);
    }

    double res = d / maxt;

    cout << "Case #" << i << ": ";

    printf("%.9lf\n", res);
  }

  return 0;
}
