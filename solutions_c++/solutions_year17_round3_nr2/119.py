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

const int MPD = 1440;
// (time of day, c's time, first element is c?, last element is c?)
int dp[MPD][MPD + 1][2][2];
int ac[MPD];
int aj[MPD];


void solve() {
  fill(&dp[0][0][0][0], &dp[0][0][0][0] + MPD * (MPD + 1) * 2 * 2, MPD);
  memset(aj, 0, sizeof(aj));
  memset(ac, 0, sizeof(ac));

  
  int AC, AJ;
  cin >> AC >> AJ;
  REP(i, AC) {
    int s, t;
    cin >> s >> t;
    REP2(j, s, t) {
      ac[j] = 1;
    }
  }
  REP(i, AJ) {
    int s, t;
    cin >> s >> t;
    REP2(j, s, t) {
      aj[j] = 1;
    }
  }

  if (!aj[0]) {
    dp[0][1][1][1] = 0;
  }

  if (!ac[0]) {
    dp[0][0][0][0] = 0;
  }

  REP2(i, 1, MPD) {
    if (!aj[i]) {
      // c's work
      REP(j, i + 1) REP(f, 2) REP(l, 2) {
        dp[i][j + 1][f][1] = min(dp[i][j + 1][f][1], dp[i - 1][j][f][l] + (l == 0));
      }
    }
    
    if (!ac[i]) {
      // j's work
      REP(j, i + 1) REP(f, 2) REP(l, 2) {
        dp[i][j][f][0] = min(dp[i][j][f][0], dp[i - 1][j][f][l] + (l == 1));
      }
    }
  }

  int res = MPD;
  REP(f, 2) REP(l, 2) res = min(res, dp[MPD - 1][MPD / 2][f][l] + (f != l));
  cout << res << endl;
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  REP(i, T) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
