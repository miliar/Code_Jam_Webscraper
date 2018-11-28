#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
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
#include <utility>
#include <vector>
using namespace std;

#endif

#ifndef MACROS

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define NL '\n'
#define SZ(c) ((int)(c).size())
#define CLR(c,v) memset(c, v, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPD(i,e) for(int i = e-1; i >= 0; --i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
#define FORC(i,c) FORU(i,c.begin(),c.end())
#define MAPI(m,e,v) if(m.find(e)!=m.end()){m[e]+=v;}else{m.insert(make_pair(e,v));}
#define SQR(x) ((x)*(x))
typedef vector<int> vi;
typedef long long Int;
typedef long double LD;
typedef pair<int,int> pii;

#endif

#ifndef TOOLS

void setup() {
  ios_base::sync_with_stdio(false);
  ios_base::fmtflags ff = cout.flags();
  ff |= cout.fixed;
  cout.flags(ff);
  cerr.precision(9);
  cout.precision(9);  
}

string ms2time(clock_t t) {
  char s[12]; int seconds = (t / CLOCKS_PER_SEC);
  sprintf(s, "%02d:%02d:%02d.%03d", seconds / 3600, (seconds % 3600) / 60, seconds % 60, t - (seconds * CLOCKS_PER_SEC));
  return string(s);
}

template <class T> T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
template <class T> string t2s(T x) {ostringstream o; o << x; return o.str();}

#endif

#define _DEBUG
#define EPS 1e-9
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define MAXN 333
#define MOD 1000000007

int T, R, C;
string CAKE[33];

void solve() {
  int rowsCovered = 0;
  REP(row,R) {
    bool notEmptyRow = false;
    REP(col,C) {
      if (CAKE[row][col] != '?') {
        notEmptyRow = true;
        int l = col, r = col;
        while (l-1 >= 0 && (CAKE[row][l-1] == '?')) { l--; CAKE[row][l] = CAKE[row][col]; }
        while (r+1  < C && (CAKE[row][r+1] == '?')) { r++; CAKE[row][r] = CAKE[row][col]; }
      }
    }
    if (notEmptyRow) { ++rowsCovered; }
  }
  while (rowsCovered != R) {
    REP(row,R) {
      if (CAKE[row][0] == '?') {
        if (row == 0 && CAKE[row+1][0] != '?') {
          ++rowsCovered; CAKE[row] = CAKE[row+1];
        } else if (row > 0 && CAKE[row-1][0] != '?') {
          ++rowsCovered; CAKE[row] = CAKE[row-1];
        } else if (row+1 < R && CAKE[row+1][0] != '?') {
          ++rowsCovered; CAKE[row] = CAKE[row+1];
        } 
      }
    }
  }
}

void readInput() {
  cin >> R >> C;
  REP(r,R) {
    cin >> CAKE[r];
  }
}

int main(int argc, char *argv[]) {
  setup();
  clock_t totalTime = clock();

  cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    clock_t caseTime = clock();
    readInput();
    solve();
    cout << "Case #" << tc << ": " << endl;
    REP(r,R) { cout << CAKE[r] << endl; }
    cerr << " [INFO] Case #" << tc << ": done in " << ms2time(clock() - caseTime) << endl;
  } 
  
  cerr << endl << " [INFO] Input done in " << ms2time(clock() - totalTime) << endl;
  return 0;
}