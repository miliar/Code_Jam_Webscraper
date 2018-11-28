#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <numeric>
#include <functional>
#include <set>
#include <map>

using namespace std;

int solve2(vector<int> groups) {
  vector<int> cntrem(10);
  for (const auto &g : groups) {
    cntrem[g % 2]++;
  }
  return cntrem[0] + ((cntrem[1] + 1) / 2);
}

int solve3(vector<int> groups) {
  vector<int> cntrem(10);
  for (const auto &g : groups) {
    cntrem[g % 3]++;
  }
  int ans = cntrem[0];
  // 1, 2
  int x = min(cntrem[1], cntrem[2]);
  cntrem[1] -= x; cntrem[2] -= x;
  ans += x;

  if (cntrem[1]) {
    ans += (cntrem[1] + 2) / 3;
  }
  if (cntrem[2]) {
    ans += (cntrem[2] + 2) / 3;
  }
  return ans;
}

int solve4(vector<int> groups) {
  vector<int> cntrem(10);
  for (const auto &g : groups) {
    cntrem[g % 4]++;
  }
  int ans = cntrem[0]; cntrem[0] = 0;
  // 1, 2, 3
  int x = min(cntrem[1], cntrem[3]);
  cntrem[1] -= x; cntrem[3] -= x;
  ans += x;

  int odd = cntrem[1] + cntrem[3];
  int even = cntrem[2];
  
  //patterns
  /*
  odd+odd+odd+odd
  odd+odd+even
  even+even
  */

  int best = 0;
  for (int use = 0; use <= even; use++) {
    // use for odd+odd+even
    int cur = 0;
    if (use * 2 > odd) {
      break;
    }
    cur += use; // odd+odd+even
    int rodd = (odd - use * 2);
    int reven = even - use;
    cur += (reven + 1) / 2; // even+even, one more even?
    if (reven % 2) { // if one remaining even, consume rodd
      rodd -= 2;
    }
    if (rodd > 0) {
      cur += (rodd + 3) / 4;
    }
    best = max(best, cur);
  }
  ans += best;
  return ans;
}


int main() {
  int TT;
  scanf("%d", &TT);
  for (int testcase = 1; testcase <= TT; testcase++) {
    int n, p;
    scanf("%d%d", &n, &p);
    vector<int> G(n);
    for (int i = 0; i < n; i++) {
      scanf("%d", &G[i]);
    }
    int ans = 0;
    if (p == 2) {
      ans = solve2(G);
    }
    else if (p == 3) {
      ans = solve3(G);
    }
    else if (p == 4) {
      ans = solve4(G);
    }
    printf("Case #%d: %d\n", testcase, ans);
  }
  return 0;
}