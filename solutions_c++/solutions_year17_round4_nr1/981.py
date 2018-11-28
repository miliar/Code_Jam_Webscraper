#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)

int n, p;
int g[100];

map<pair<vector<int>, int>, int> dp;

int solve(vector<int> &v, int r) {
  pair<vector<int>, int> s = MP(v, r);
  if (dp.count(s))
    return dp[s];
  int tot = 0;
  for (auto &x: v) tot += x;
  if (!tot)
    return 0;

  int ret = 0;
  REP (i, p) {
    if (v[i] == 0)
      continue;
    --v[i];
    int nr = ((i - r) % p + p) % p;
    ret = max(ret, solve(v, (p-nr) % p));
    ++v[i];
  }
  return dp[s] = ret + (r == 0);
}

void solve() {
  dp.clear();

  cin >> n >> p;
  vector<int> v(p);

  REP (i, n) {
    cin >> g[i];
    g[i] %= p;
    v[g[i]]++;
  }

  cout << solve(v, 0) << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int T;
  cin >> T;
  REP (i, T) {
    cerr << "Case #" << i+1 << ": " << endl;
    cout << "Case #" << i+1 << ": ";
    solve();
  }

  return 0;
}
