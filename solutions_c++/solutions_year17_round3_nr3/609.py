#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define SQR(x) ((x) * (x))
#define PI (acos(-1))
#define eps (1e-9)

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

int n, k, x, p[111];

priority_queue<int, vector<int>, greater<int> > heap;

int cmp(double a, double b) {
  if (abs(a - b) <= eps) {
    return 0;
  }

  if (a < b) {
    return -1;
  }

  return 1;
}

int main() {
  int t;
  cin >> t;

  FOR (test, 1, t) {
    cout << "Case #" << test << ": ";

    cin >> n >> k;
    double tmp;
    cin >> tmp;
    x = (int) (tmp * 10000 + eps);

    FOR (i, 1, n) {
      cin >> tmp;
      p[i] = (int) (tmp * 10000 + eps);
    }

    FOR (i, 1, n) heap.push(p[i]);
    while (x > 0) {
      x--;
      int minP = heap.top(); heap.pop();
      heap.push(minP + 1);
    }

    double res = 1.0;
    while (!heap.empty()) {
      int p = heap.top(); heap.pop();
      res *= p / 10000.0;
    }

    printf("%.9lf\n",res);

  }
}
