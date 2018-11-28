#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

LL n, k;

void solve(int tc) {
  cin >> n >> k;
  cout << "Case #" << tc << ": ";
  map<LL, LL> mp;
  mp.insert(MP(-n, 1));
  while (true) {
    LL m = -mp.begin()->first;
    LL cnt = mp.begin()->second;
    mp.erase(mp.begin());

    LL l = (m-1) / 2;
    LL r = (m-1) / 2;

    if (l + r != m-1) r++;

    if (cnt >= k) {
      cout << r << ' ' << l << endl;
      return;
    }

    k -= cnt;

    if (l) mp[-l] += cnt;
    if (r) mp[-r] += cnt;
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  FOR(i, tt) {
    solve(i+1);
  }
  return 0;
}


