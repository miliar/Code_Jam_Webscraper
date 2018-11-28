#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstring>
#include <cstdarg>
#include <cstdio>
#include <random>
#include <cmath>
#include <ctime>
#include <functional>
#include <algorithm>
#include <complex>
#include <numeric>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <array>
#include <list>
#include <map>
#include <set>
using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) int((a).size())
#define MP(x, y) make_pair((x),(y))
#define FI first
#define SE second
#define LOWB(x) (x & (-x))
#define UNIQUE(a) sort(ALL(a)), (a).erase(unique(ALL(a)), (a).end())
#define HEIGHT(n) (sizeof(int) * 8 - __builtin_clz(n)) //height of range n segment tree
#define INF 1e9
#define INF_LL 4e18
#define rep(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
/*-----------------------------------*/
int n, r, o, y, g, b, v;

string simple(char c) {
  string ans = "";
  for (int i=0; i<n; i+=2) {
    if (c != 'r') ans.push_back('R');
    if (c != 'y') ans.push_back('Y');
    if (c != 'b') ans.push_back('B');
  }
  return ans;
}

string solve_sml() {
  if (r > y + b ||
      y > r + b ||
      b > r + y) return "IMPOSSIBLE";
  if (r == 0) return simple('r');
  if (y == 0) return simple('y');
  if (b == 0) return simple('b');
  string ans = "R";
  for (int i=1; i<r; i++) {
    if (y > b) {
      ans.push_back('Y');
      y--;
    } else {
      ans.push_back('B');
      b--;
    }
    ans.push_back('R');
  }
  if (abs(y - b) > 1) return "IMPOSSIBLE";
  if (y >= b) {
    for (int i=0; i<b; i++) {
      ans.push_back('Y');
      ans.push_back('B');
    }
    if (y > b) ans.push_back('Y');
  } else {
    for (int i=0; i<y; i++) {
      ans.push_back('B');
      ans.push_back('Y');
    }
    ans.push_back('B');
  }
  return ans;
}

string solve_large() {
  return "IMPOSSIBLE";
}

string solve() {
  cin >> n >> r >> o >> y >> g >> b >> v;
  return solve_sml();
}

bool verify(string ans) {
  if (SZ(ans) != n) return false;
  if (n == 1) return true;
  for (int i=0; i<n; i++) {
    if (ans[i] == ans[(i+1)%n]) {
      cout << ans << endl;
      return false;
    }
  }
  return true;
}

int main() {
  int cas;
  cin >> cas;
  for (int i=1; i<=cas; i++) {
    string ans = solve();
    if (ans != "IMPOSSIBLE" && !verify(ans)) {
      assert(false);
    }
    printf("Case #%d: %s\n", i, ans.c_str());
  }
  return 0;
}
