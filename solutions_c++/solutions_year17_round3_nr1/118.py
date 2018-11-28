#include <bits/stdc++.h>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <tuple>
#include <typeinfo>
#include <unordered_set>
#include <unordered_map>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REPD(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define PB(e) push_back(e)
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define MP(a, b) make_pair(a, b)
#define BIT(n, m) (((n) >> (m)) & 1)

const double PI = 4 * atan(1.0);
typedef long long ll;

template <typename S, typename T> ostream &operator<<(ostream &out, const pair<S, T> &p) {
  out << "(" << p.first << ", " << p.second << ")";
  return out;
}

template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  out << "[";
  REP(i, v.size()){
    if (i > 0) out << ", ";
    out << v[i];
  }
  out << "]";
  return out;
}

double surface_area(double r, double h) {
  return 2 * r * PI * h;
}

double circle_area(double r) {
  return PI * r * r;
}


void solve() {
  int N, K;
  cin >> N >> K;
  vector<pair<ll, ll> > ps(N);
  vector<vector<double> > dp(N + 1, vector<double>(K +  1, -1e300));
  REP(i, N) cin >> ps[i].first >> ps[i].second;
  sort(ALL(ps));
  
  dp[0][0] = 0;
  REP(i, N) {
    REP(j, K + 1) {
      dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
      if (j > 0) {
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + surface_area(ps[i].first, ps[i].second) + (j == K ? circle_area(ps[i].first) : 0));
      }
    }
  }
  cout <<fixed << setprecision(20) << dp[N][K] << endl;
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  REP(i, T) {
    cout <<  "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
