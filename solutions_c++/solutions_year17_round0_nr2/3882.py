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

int T;
string S;

int main(void) {
  cin >> T;
  REP(t, T) {
    cin >> S;
    REP(i, SIZE(S)) S[i] -= '0';
    REP(k, SIZE(S)-1) {
      if (S[k] > S[k+1]) {
        while(k >= 0) {
          S[k] -= 1;
          if (k == 0) break;
          if (S[k-1] <= S[k]) break;
          --k;
        }
        for(int i=k+1; i<SIZE(S); ++i) S[i] = 9;
        break;
      }
    }
    cout << "Case #" << (t+1) << ": ";
    bool start = false;
    REP(i, SIZE(S)) {
      if (S[i] == 0 && !start) continue;
      start = true;
      cout << (char)(S[i] + '0');
    }
    cout << endl;
  }
  return 0;
}
