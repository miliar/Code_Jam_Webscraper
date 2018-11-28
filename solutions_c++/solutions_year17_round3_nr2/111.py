#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; }
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; }
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

const int INF = 1000 * 1000;
const int UNITS = 1440;
int dp[UNITS + 1][UNITS / 2 + 1][2][2];

void solve(int tc) {
  int a, b;
  cin >> a >> b;

  vector<int> day(UNITS, -1);

  FOR(i, 0, a) {
    int x, y;
    cin >> x >> y;
    FOR(j, x, y) {
      day[j] = 0;
    }
  }

  FOR(i, 0, b) {
    int x, y;
    cin >> x >> y;
    FOR(j, x, y) {
      day[j] = 1;
    }
  }

  memset(dp, 0, sizeof dp);

  FOR(i, 0, UNITS / 2 + 1) {
    dp[0][i][0][0] = dp[0][i][1][1] = i ? INF : 0;
    dp[0][i][1][0] = dp[0][i][0][1] = i ? INF : 1;
  }

  // FOR(t, 1, UNITS + 1) {
  //   FOR(w, 0, UNITS / 2 + 1) {
  //     if (w > t) {
  //       dp[t][w][0] = dp[t][w][1] = INF;
  //     }
  //   }
  // }

  FOR(t, 1, UNITS + 1) {
    FOR(w, 0, UNITS / 2 + 1) {
      FOR(p, 0, 2) {
        FOR(q, 0, 2) {
          int &result = dp[t][w][p][q];
          int today = day[t - 1];
          result = INF;
          if (today != 1 && w > 0) {
            smin(result, dp[t - 1][w - 1][0][q] + (p != 0));
          }
          if (today != 0) {
            smin(result, dp[t - 1][w][1][q] + (p != 1));
          }
        }
      }
    }
  }

  cout << fixed << setprecision(8);
  cout << "Case #" << tc << ": ";
  cout << min(dp[UNITS][UNITS / 2][0][0], dp[UNITS][UNITS / 2][1][1]);
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  FOR(l, 1, t + 1) {
    solve(l);
  }
  return 0;
}
