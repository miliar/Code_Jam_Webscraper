#include <bits/stdc++.h>

using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REPD(i, n) for (int i = (n) - 1; i >= 0; i--)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)

#define RESET(c, x) memset(c, x, sizeof(c))
#define BUG(x) { auto _ = (x); cerr << #x << " = " << _ << endl; }
#define PR0(a, n) { cerr << #a <<" = "; REP(_,n) cerr << a[_] << ' '; cerr << endl; }
#define PR1(a, n) { cerr << #a <<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr << endl; }

typedef long long ll;
typedef pair<int, int> pii;

/******************************************************************************/

#define EPS 1e-8
vector<pair<double, int> > a;
double d;
int n;

double solve() {
  double time = 0;
  int fin = 0;
  sort(a.rbegin(), a.rend());
  while (fin < n) {
    double step = (d - a[fin].first) / a[fin].second;
    for (int i = fin + 1; i < n; i++) {
      int j = i - 1;
      if (a[i].second <= a[j].second) continue;
      double delta = (a[j].first - a[i].first) / (a[i].second - a[j].second);
      if (delta > 0 && delta < step) step = delta;
    }
    if (step <= 0) {
      time += (d - a[n - 1].first) / a[n - 1].second;
      fin = n;
      break;
    }
    for (int i = fin; i < n; i++) {
      a[i].first += a[i].second * step;
      if (i <= fin) continue;
      int j = i - 1;
      if (a[i].first - a[j].first > -EPS) a[i].second = a[j].second;
    }
    while (fin < n && a[fin].first >= d) fin++;
    time += step;
  }
  return d / time;
}

int main() {
  cout.setf(ios_base::fixed, ios_base::floatfield);
  cout.precision(6);

  int tests;
  double k; int s;
  cin >> tests;
  for (int test = 1; test <= tests; test++) {
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
      cin >> k >> s;
      a.push_back(make_pair(k, s));
    }
    double result = solve();
    cout << "Case #" << test << ": " << result << endl;
    a.clear();
  }
}
