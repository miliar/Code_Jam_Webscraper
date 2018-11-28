#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

// #ifdef ONLINE_JUDGE
// #define freopen if(0)freopen
// #else
// #define cerr if(0)cerr
// #endif

#define fe first
#define se second
#define pb push_back
#define mp make_pair
#define FILENAME ""
#define inf 2000000000
#define mod 1000000007
#define ll long long
using namespace std;

pair<int, int> solve(int n, int k) {
  vector<bool> u(n + 2);
  vector< pair<int, int> > v(n + 2);
  for (int i = 0; i < n + 2; i++) {
      u[i] = false;
      v[i] = make_pair(0, 0);
  }
  u[0] = u[n + 1] = true;

  int mx1, mx2, cnt, id;
  for (int j = 1; j <= k; j++) {
    for (int i = 0; i < n + 2; i++) v[i] = make_pair(0, 0);
    for (int i = 1; i <= n; i++) {
      int x = i - 1, y = i + 1;
      while (!u[x]) v[i].first++, x--;
      while (!u[y]) v[i].second++, y++;
    }
    mx1 = -inf, mx2 = -inf, cnt = 0, id = -1;
    for (int i = 1; i <= n; i++)
      if (!u[i])
        mx1 = max(mx1, min(v[i].first, v[i].second));
    for (int i = 1; i <= n; i++)
      if (!u[i] && min(v[i].first, v[i].second) == mx1)
        cnt++, id = i;
    if (cnt > 1) {
      for (int i = 1; i <= n; i++)
        if (!u[i] && min(v[i].first, v[i].second) == mx1)
          mx2 = max(mx2, max(v[i].first, v[i].second));
      for (int i = n; i >= 1; i--)
        if (!u[i]
          && min(v[i].first, v[i].second) == mx1
          && max(v[i].first, v[i].second) == mx2)
          id = i;
    }
    u[id] = true;
  }
  for (int i = 0; i < n + 2; i++) v[i] = make_pair(0, 0);
  for (int i = 1; i <= n; i++) {
    int x = i - 1, y = i + 1;
    while (!u[x]) v[i].first++, x--;
    while (!u[y]) v[i].second++, y++;
  }
  return make_pair(max(v[id].first, v[id].second),
                    min(v[id].first, v[id].second));
}

int main() {
  // freopen(".in","r",stdin);
  // freopen("output.txt","w",stdout);
  int T;
  int N, K;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    cin >> N >> K;
    pair<int, int> ans = solve(N, K);
    cout << "Case #" << i << ": " << ans.first << " " << ans.second << endl;
  }

  return 0;
}













//
