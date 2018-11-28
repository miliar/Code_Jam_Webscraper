#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

int T, K;
string S;
int p;

int main(void) {
  cin >> T;
  REP(t, T) {
    p = 0;
    cin >> S >> K;
    vector<int> V(SIZE(S), 0);
    REP(i, SIZE(S)) V[i] = (S[i] == '+');
    
    cout << "Case #" << (t+1) << ": ";
    REP(i, SIZE(V)) {
      if (V[i] == 1) continue;
      if (i+K > SIZE(V)) {
        cout << "IMPOSSIBLE" << endl;
        p = -1;
        break;
      }
      REP(k, K) V[i+k] = 1 - V[i+k];
      ++p;
    }
    if (p >= 0) cout << p << endl;
  }
  return 0;
}
