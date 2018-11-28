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


bool check[256][256];
unordered_set<long long> vis[256];

void init() {
  memset(check, 0, sizeof(check));
  check['R']['G'] = check['G']['R'] = true;
  check['R']['Y'] = check['Y']['R'] = true;
  check['R']['B'] = check['B']['R'] = true;  
  check['B']['Y'] = check['Y']['B'] = true;
  check['V']['Y'] = check['Y']['V'] = true;
  check['B']['O'] = check['O']['B'] = true;
}

long long encode(int r, int o, int y, int g, int b, int v) {
  long long x = 0;
  x = 1001 * x + r;
  x = 1001 * x + o;
  x = 1001 * x + y;
  x = 1001 * x + g;
  x = 1001 * x + b;
  x = 1001 * x + v;
  return x;
}

bool dfs(string &s, int r, int o, int y, int g, int b, int v) {
  long long en = encode(r, o, y, g, b, v);


  if (r + o + y + g + b + v == 0) {
    if (s.length() == 1)
      return true;
    char x = s.front();
    char y = s.back();
    return check[x][y];
  }

  if (s.size() && vis[s.back()].count(en))
    return false;

  if (!s.size()) {
    if (r > 0) {
      s += 'R';
      if (dfs(s, r-1, o, y, g, b, v))
        return true;
      s.pop_back();
    }
    if (o > 0) {
      s += 'O';
      if (dfs(s, r, o-1, y, g, b, v))
        return true;
      s.pop_back();
    }
    if (y > 0) {
      s += 'Y';
      if (dfs(s, r, o, y-1, g, b, v))
        return true;
      s.pop_back();
    }
    if (g > 0) {
      s += 'G';
      if (dfs(s, r, o, y, g-1, b, v))
        return true;
      s.pop_back();
    }
    if (b > 0) {
      s += 'B';
      if (dfs(s, r, o, y, g, b-1, v))
        return true;
      s.pop_back();
    }
    if (v > 0) {
      s += 'V';
      if (dfs(s, r, o, y, g, b, v-1))
        return true;
      s.pop_back();
    }
  } else {
    char pre = s.back();
    if (r > 0 && check['R'][pre]) {
      s += 'R';
      if (dfs(s, r-1, o, y, g, b, v))
        return true;
      s.pop_back();
    }
    if (o > 0 && check['O'][pre]) {
      s += 'O';
      if (dfs(s, r, o-1, y, g, b, v))
        return true;
      s.pop_back();
    }
    if (y > 0 && check['Y'][pre]) {
      s += 'Y';
      if (dfs(s, r, o, y-1, g, b, v))
        return true;
      s.pop_back();
    }
    if (g > 0 && check['G'][pre]) {
      s += 'G';
      if (dfs(s, r, o, y, g-1, b, v))
        return true;
      s.pop_back();
    }
    if (b > 0 && check['B'][pre]) {
      s += 'B';
      if (dfs(s, r, o, y, g, b-1, v))
        return true;
      s.pop_back();
    }
    if (v > 0 && check['V'][pre]) {
      s += 'V';
      if (dfs(s, r, o, y, g, b, v-1))
        return true;
      s.pop_back();
    }
  }

  if (s.size())
    vis[s.back()].insert(en);
  return false;
}

void solve() {
  int n, r, o, y, g, b, v;
  cin >> n >> r >> o >> y >> g >> b >> v;
  REP (i, 256)
    vis[i].clear();
  string ret = "";

  if (dfs(ret, r, o, y, g, b, v))
    cout << ret << endl;
  else
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    init();
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
