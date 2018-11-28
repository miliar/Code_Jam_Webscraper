#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

struct line { ll m, c; };

bool cmp(const line &a, const line &b) {
  if (a.m != b.m) return a.m > b.m;
  return a.c < b.c;
}

int main() {
  int T;
  cin >> T;
  REP (tc, T) {
    int N;
    double D;
    cin >> D >> N;

    vector<line> lines;

    FOR (i, N) {
      ll K, S;
      cin >> K >> S;
      lines.push_back(line {S, K});
    }
    sort(lines.begin(), lines.end(), cmp);

    vector<line> hull;
    for (auto c : lines) {
      while (hull.size() >= 2) {
        line a = hull[hull.size() - 2], b = hull[hull.size() - 1];
        if ((a.m - c.m) * (b.c - a.c) < (a.m - b.m) * (c.c - a.c))
          break;
        hull.pop_back();
      }

      hull.push_back(c);
    }

    int i = 0;
    while (i + 1 < hull.size()) {
      line a = hull[i], b = hull[i + 1];
      if (a.m * (b.c - a.c) + a.c * (a.m - b.m) > D * (a.m - b.m))
        break;
      ++i;
    }

    double arrival = (D - hull[i].c) / hull[i].m;
    cout << "Case #" << tc << ": ";
    cout << fixed << setprecision(9) << (D / arrival) << endl;
  }
  return 0;
}
