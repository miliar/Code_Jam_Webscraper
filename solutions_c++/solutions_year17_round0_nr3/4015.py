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

int T, N, K;
int d, ls, rs;

int main(void) {
  cin >> T;
  REP(t, T) {
    set<pair<int,int> > S;
    cin >> N >> K;
    S.insert(make_pair(N, 0));
    while(K > 0) {
      pair<int, int> P = *S.rbegin();
      S.erase(--S.end());
      d = P.first - 1;
      ls = d/2;
      rs = (d+1)/2;
      if (ls > 0) S.insert(make_pair(ls, P.second));
      if (rs > 0) S.insert(make_pair(rs, P.second + ls + 1));
      --K;
    }
    cout << "Case #" << (t+1) << ": " << max(ls, rs) << " " << min(ls, rs) << endl;
  }
  return 0;
}
