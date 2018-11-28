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
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORC(i,c) FORU(i,c.begin(),c.end())
#define SQR(x) ((x)*(x))
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
  cerr.precision(6);
  cout.precision(6);  
}

string ms2time(clock_t t) {
  char s[12]; int seconds = (t / CLOCKS_PER_SEC);
  sprintf(s, "%02d:%02d:%02d.%03d", seconds / 3600, (seconds % 3600) / 60, seconds % 60, (int)(t - (seconds * CLOCKS_PER_SEC)));
  return string(s);
}

template <class T> ostream& operator<< (ostream& os, vector<T> x) { REP(i,SZ(x)) { os << x[i] << " "; } return os; }
template <class T> T s2t(string s) { istringstream i(s); T x; i>>x; return x; }
template <class T> string t2s(T x) { ostringstream o; o << x; return o.str(); }

vector<string> split (string s, string del = " ") { vector<string> res;
  int ss = s.size(), sdel = del.size();
  for (int p = 0, q; p < ss; p = q+sdel) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
    if (q-p>0) res.push_back(s.substr(p,q-p));
  } return res;
}

vector<int> splitInts (string s, string del = " ") { vector<int> res;
  vector<string> t = split(s,del);
  for (int i = 0; i < (signed)t.size(); ++i) {
    if (t[i].size() > 10 || (t[i].size()==10 && t[i][0]>='2')) {
      res.push_back(2000000000);
    } else { res.push_back(atoi(t[i].c_str())); }
  } return res;
}

#endif

#define EPS 1e-9
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define MAXN 333
#define MOD 1000000007

Int T, D, N;
Int K[1010];
Int S[1010];

LD solve() {
  LD result = 0.0, maxTime = 0.0;
  REP(i,N) {
    LD T = (LD)(D - K[i]) / S[i];
    maxTime = max(maxTime, T);
    cerr << i << ": " << T << endl;
  }
  
  cerr << "maxTime: " << maxTime << endl;
  return D / maxTime;
}

void readInput() {
  cin >> D >> N;
  REP(i,N) {
    cin >> K[i] >> S[i];
  }
}

int main() {
  setup();
  clock_t totalTime = clock();

  cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    clock_t caseTime = clock();
    readInput();
    LD result = solve();
    cout << "Case #" << tc << ": " << result << endl;
    cerr << "Case #" << tc << ": " << result << endl;
    cerr << " [INFO] Case #" << tc << ": done in " << ms2time(clock() - caseTime) << endl;
  } 
  
  cerr << endl << " [INFO] Input done in " << ms2time(clock() - totalTime) << endl;
  return 0;
}