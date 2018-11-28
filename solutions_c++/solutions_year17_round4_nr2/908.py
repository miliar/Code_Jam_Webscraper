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

int n, c, m;
void solve() {
  cin >> n >> c >> m;
  vector<int> v1, v2;
  REP (i, m) {
    int p, b;
    cin >> p >> b;
    if (b == 1)
      v1.push_back(p);
    else
      v2.push_back(p);
  }

  int x = 0;
  int y = 0;
  sort(ALL(v1));
  sort(ALL(v2));
  while (v1.size() && v2.size()) {
    bool done = false;
    // from v1
    REP (i, v2.size()) {
      if (v1[0] < v2[i]) {
        ++x;
        v1.erase(v1.begin());
        v2.erase(v2.begin()+i);
        done = true;
        break;
      }
    }
    if (done) continue;

    // from v2
    REP (i, v1.size()) {
      if (v2[0] < v1[i]) {
        ++x;
        v1.erase(v1.begin() + i);
        v2.erase(v2.begin());
        done = true;
        break;
      }
    }
    if (done) continue;

    // double head
    if (v1[0] == 1 && v2[0] == 1) {
      x += 2;
      v1.pop_back();
      v2.pop_back();
    } else {
      ++x;
      ++y;
      v1.pop_back();
      v2.pop_back();
    }
  }

  x += v1.size() + v2.size();
  cout << x << " " << y << endl;
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
