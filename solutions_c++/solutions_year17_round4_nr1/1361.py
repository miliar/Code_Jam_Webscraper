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

int T, N, P, x, l, ret;

int main(void) {
  cin >> T;
  REP(t, T) {
    cin >> N >> P;
    ret = 0;
    vector<int> m(P, 0);
    REP(n, N) {
      cin >> x;
      if (x % P == 0) ++ret;
      else ++m[x%P];
    }
    if (P == 2) {
      ret += (m[1] + 1) / 2;
    }
    if (P == 3) {
      l = min(m[1], m[2]);
      ret += l;
      m[1] -= l;
      m[2] -= l;
      ret += (m[1] + 2) / 3;
      ret += (m[2] + 2) / 3;
    }
    if (P == 4) {
      l = min(m[1], m[3]);
      ret += l;
      m[1] -= l;
      m[3] -= l;
      ret += (m[2] / 2);
      m[2] -= (m[2]/2)*2;
      if (m[2] > 0) {
        ++ret;
        m[1] -= 2;
        m[3] -= 2;
      }
      if (m[1] > 0) ret += (m[1] + 3) / 4;
      if (m[3] > 0) ret += (m[3] + 3) / 4;
    }
    cout << "Case #" << (t+1) << ": " << ret << endl;
  }
  return 0;
}
