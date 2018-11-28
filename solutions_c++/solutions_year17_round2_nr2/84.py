#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string problemName = "B";
string smallFileName = problemName + "-small-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

string order(char q, char w, int n) {
  string s;
  REP (i, n) {
    s += q;
    s += w;
  }
  return s;
}

string solve(int n, int r, int o, int y, int g, int b, int v) {
  if (n == b + o && b == o) {
    return order('B', 'O', b);
  }
  if (n == r + g && r == g) {
    return order('R', 'G', r);
  }
  if (n == y + v && y == v) {
    return order('Y', 'V', y);
  }
  b -= o;
  r -= g;
  y -= v;
  if (b < 0 || r < 0 || y < 0) {
    return "IMPOSSIBLE";
  }
  string s;
  while (r || b || y) {
    vi cnt{r, b, y};
    int best = -1;
    string f = "RBY";
    REP (i, 3) {
      if (sz(s) && s.back() == f[i]) continue;
      if (!cnt[i]) continue;
      if (best == -1 || cnt[i] > cnt[best] || (cnt[i] == cnt[best] && sz(s) && s[0] == f[i]))
	best = i;
    }

    if (best == -1) break;
    if (best == 0) {
      s += 'R';
      --r;
      while (g) {
	s += "GR";
	--g;
      }
      continue;
    }
    if (best == 1) {
      s += 'B';
      --b;
      while (o) {
	s += "OB";
	--o;
      }
      continue;
    }
    if (best == 2) {
      s += 'Y';
      --y;
      while (v) {
	s += "VY";
	--v;
      }
      continue;
    }
    break;
  }
  if (s[0] == s.back() || sz(s) != n) {
    return "IMPOSSIBLE";
  }
  return s;
}

string found = "";

bool can(char q, char w) {
  if (q == w) return false;
  if (q == 'O' && w != 'B') return false;
  if (w == 'O' && q != 'B') return false;
  if (q == 'G' && w != 'R') return false;
  if (w == 'G' && q != 'R') return false;
  if (q == 'V' && w != 'Y') return false;
  if (w == 'V' && q != 'Y') return false;
  return true;
}

bool rec(int n, int r, int o, int y, int g, int b, int v, string s) {
  if (n == 0) {
    if (can(s[0], s.back())) {
      found = s;
      return true;
    }
    return false;
  }
  if (!sz(s) || can(s.back(), 'R')) {
    if (r && rec(n-1, r-1, o, y, g, b, v, s + 'R')) return true;
  }
  if (!sz(s) || can(s.back(), 'O')) {
    if (o && rec(n-1, r, o-1, y, g, b, v, s + 'O')) return true;
  }
  if (!sz(s) || can(s.back(), 'Y')) {
    if (y && rec(n-1, r, o, y-1, g, b, v, s + 'Y')) return true;
  }
  if (!sz(s) || can(s.back(), 'G')) {
    if (g && rec(n-1, r, o, y, g-1, b, v, s + 'G')) return true;
  }
  if (!sz(s) || can(s.back(), 'B')) {
    if (b && rec(n-1, r, o, y, g, b-1, v, s + 'B')) return true;
  }
  if (!sz(s) || can(s.back(), 'V')) {
    if (v && rec(n-1, r, o, y, g, b, v-1, s + 'V')) return true;
  }
  return false;
}

bool validate(string s) {
  REP (i, sz (s)-1) {
    if (!can(s[i], s[i+1])) return false;
  }
  if (!can(s[0], s.back())) return false;
  return true;
}

bool check(int n, int r, int o, int y, int g, int b, int v) {
  string res1 = solve(n, r, o, y, g, b, v);
  bool res2 = rec(n, r, o, y, g, b, v, "");
  if (res1 == "IMPOSSIBLE" && !res2) {
    return true;
  }
  if (res1 == "IMPOSSIBLE" && res2) {
    cout << "Solution exist " << found << endl;
    return false;
  }
  if (!validate(res1)) {
    cout << res1 << " is incorrect answer\n";
    if (res2) {
      cout << "Solution " + found << endl;
    } else {
      cout << "Solution doesn't exist" << endl;
    }
    return false;
  }
  return true;
}

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    // REP (r, 10) {
    //   REP (o, 10) {
    // 	REP (y, 10) {
    // 	  REP (g, 10) {
    // 	    REP (b, 10) {
    // 	      REP (v, 10) {
    // 		if (r+o+y+g+b+v < 15 && r+o+y+g+b+v >= 3) {
    // 		  if (!check(r+o+y+g+b+v, r, o, y, g, b, v)) {
    // 		    cout << r << ' ' << o << ' ' << y << ' ' << g << ' ' << b << ' ' << v << endl;
    // 		    return 1;
    // 		  } else {
    // 		    cout << "PASSED" << endl;
    // 		  }
    // 		}
    // 	      }
    // 	    }
    // 	  }
    // 	}
    //   }
    // }
    int T;
    cin >> T;
    REP (test, T) {
	cout << "Case #" << (test + 1) << ": ";
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	cout << solve(n, r, o, y, g, b, v) << endl;
	//	check(n, r, o, y, g, b, v);
    }
    return 0;
}
