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

bool isTidy(long long x) {
  int last = 9;
  while (x) {
    if (x % 10 > last)
      return false;
    last = x % 10;
    x /= 10;
  }
  return true;
}

long long slow(long long x) {
  while (!isTidy(x))
    --x;
  return x;
}

long long fast(long long x) {
  vector<int> d;
  while (x) {
    d.pb(x % 10);
    x /= 10;
  }
  reverse(d.begin(), d.end());
  int len = (int) d.size();
  long long ans = 0;
  for (int i = 0; i < len; i++) {
    bool ok = true;
    for (int j = i + 1; j < len; j++) {
      if (d[i] < d[j])
        break;
      if (d[i] > d[j])
        ok = false;
    }
    if (ok)
      ans = ans * 10ll + d[i];
    else {
      ans = ans * 10ll + d[i] - 1;
      for (int j = i + 1; j < len; j++)
        ans = ans * 10ll + 9;
      break;
    }
  }
  return ans;
}

void solve() {
  long long n;
  scanf("%lld", &n);
  long long res = fast(n);
  //assert(res == slow(n));
  printf("%lld\n", res);
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