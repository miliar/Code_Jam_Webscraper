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

void solve() {
  long long n, k, x;
  map<long long, long long> cnt;

  cin >> n >> k;
  cnt[n] = 1;
  
  for (long long b = 1; b <= n; b <<= 1) {
    if (k <= b) {
      vector<tuple<long long, long long> > v(ALL(cnt));
      sort(v.rbegin(), v.rend());
      if (k <= get<1>(v[0])) {
        x = get<0>(v[0]);
      } else {
        x = get<0>(v[1]);
      }
      break;
    }
    k -= b;
    map<long long, long long> nxt;
    for (auto &pr : cnt) {
      long long v = (pr.first-1);
      long long w = pr.second;
      if (v/2 > 0)
        nxt[v/2] += w;
      if (v - v/2 > 0)
        nxt[v - v/2] += w;
    }
    cnt = nxt;
  }
  --x;
  cout << x-x/2 << " " << x/2 << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
