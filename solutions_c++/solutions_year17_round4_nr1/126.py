#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

int mem[101][101][101][4];

#define update(x, y, z, t) (mem[x][y][z][t] == -1 ? solve(x, y, z, t) : mem[x][y][z][t])

int n, p;

int solve(int c1, int c2, int c3, int rem) {
  int best = 0;
  if (c1 > 0) {
    int nr = (rem + p - 1) % p;
    int res = update(c1 - 1, c2, c3, nr);
    res += (rem == 0);
    best = max(best, res);
  }

  if (c2 > 0) {
    int nr = (rem + p - 2) % p;
    int res = update(c1, c2 - 1, c3, nr);
    res += (rem == 0);
    best = max(best, res);
  }

  if (c3 > 0) {
    int nr = (rem + p - 3) % p;
    int res = update(c1, c2, c3 - 1, nr);
    res += (rem == 0);
    best = max(best, res);
  }

  return mem[c1][c2][c3][rem] = best;
}

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    cerr << "Processing case " << it << endl;
    cin >> n >> p;

    int cnt[4] = {0};
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int temp;
      scanf("%d", &temp);
      if (temp % p == 0) {
        ans++;
      } else {
        cnt[temp % p]++;
      }
    }
    memset(mem, -1, sizeof(mem));
    ans += solve(cnt[1], cnt[2], cnt[3], 0);
    cout << "Case #" << it << ": " << ans << endl;
  }
  return 0;
}
