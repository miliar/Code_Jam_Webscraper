/* prosto beresh' i jahaesh' */

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

#define f first
#define s second

#define pb push_back
#define mp make_pair

using namespace std;

const int N = (int) 1e6 + 7;
const int MOD = (int) 1e9 + 7;

void solve() {
  long long n, k;
  cin >> n >> k;
  map<long long, long long> cnt;
  cnt[n] = 1;
  while (k > 0) {
    long long len = cnt.rbegin() -> f;
    long long f = cnt[len];
    f = min(f, k);
    k -= f;
    cnt[len / 2] += f;
    cnt[(len - 1) / 2] += f;
    cnt[len] -= f;
    if (cnt[len] == 0)
      cnt.erase(len);
    if (k == 0) {
      cout << len / 2 << ' ' << (len - 1) / 2 << endl;
    }
  }
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; cases++) {
    printf("Case #%d: ", cases);
    solve();
    cerr << cases << " done\n";
  }


  return 0;
}