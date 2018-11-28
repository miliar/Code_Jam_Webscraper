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

template<class T> ostream& operator << (ostream& os, vector<T> vec) {
    for(int i=0; i<(signed)vec.size(); ++i) {
        os << vec[i] << " ";
    }
    return os;
}

#endif

struct comp { // Checks whether e1 is less than e2
  bool operator () (const pii e1, const pii e2) {
    Int eld = e1.ND - e1.ST;
    Int e2d = e2.ND - e2.ST;
    if (eld < e2d) return true;
    if (eld > e2d) return false;
    return e1.ST > e2.ST;
  }
};

Int T, N, K;
Int y, z;

// empty intervals (start, end); largest @ top
priority_queue<pii,vector<pii>,comp> PQ;

void readInput() {
  cin >> N >> K;
}

void solve() {
  while (!PQ.empty()) PQ.pop();
  PQ.push(MP(1,N));
  Int occStall = 0;
  while (occStall < K && !PQ.empty()) {
    pii interval = PQ.top(); PQ.pop();
    //cout << "POP:" << interval.ST << "-" << interval.ND << endl;
    int stallIdx = interval.ST + ((interval.ND - interval.ST) >> 1);
    int LS = stallIdx - interval.ST;
    int RS = interval.ND - stallIdx;
    y = max(LS,RS);
    z = min(LS,RS);
    //cout << (occStall+1) << ": " << stallIdx << " (" << y << "," << z << ")" << endl;
    if (interval.ST <= stallIdx-1) { 
      PQ.push(MP(interval.ST,stallIdx-1)); /*cout << "PUSH: " << interval.ST << "-" << stallIdx-1 << endl;*/ 
    }
    if (stallIdx+1 <= interval.ND) { 
      PQ.push(MP(stallIdx+1,interval.ND)); /*cout << "PUSH: " << stallIdx+1 << "-" << interval.ND << endl;*/ 
    }
    ++occStall;
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
    cout << "Case #" << tc << ": " << y << " " << z << endl;
    cerr << " [INFO] Case #" << tc << ": done in " << ms2time(clock() - caseTime) << endl;
  } 
  
  cerr << endl << " [INFO] Input done in " << ms2time(clock() - totalTime) << endl;
  return 0;
}