#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

const int MAXN = 25;
const double eps = 1e-12;

int tn;
int n, p;
int need[MAXN];
int a[MAXN][MAXN];
int from[MAXN][MAXN];
int to[MAXN][MAXN];

bool can(int x, int nd, int num) {
  long long total = 1ll * nd * num;
  return 1.0 * x + eps >= 0.9 * total && 1.0 * x <= 1.1 * total + eps;
}

pair <int, int> rng(int x, int nd) {
  int nl = -1, nr = -1;

  //cout << "H1" << endl;
  
  int l = 0, r = 2 * 1e6;
  while (l < r) {
    int mid = (l + r + 1) / 2;
    if (0.9 * mid * nd <= 1.0 * x + eps) {
      l = mid;
    } else {
      r = mid - 1;
    }
  } 
  nr = l;

  //cout << "H2" << endl;

  l = 0, r = 2 * 1e6;
  while (l < r) {
    int mid = (l + r) / 2;
    if (1.1 * mid * nd + eps >=  1.0 * x) {
      r = mid;
    } else {
      l = mid + 1;
    }
  }
  nl = l;

  //cout << "H3" << endl;

  if (nl == 0) {
    nl++;
  }
  if (nr == 0) {
    nr--;
  }

  if (nl > nr) {
    return make_pair(-1, -1);
  } else {
    return make_pair(nl, nr);
  }
}

bool cross(int l, int r, int ll, int rr) {
  if (l == -1 || ll == -1) {
    return false;
  }
  if (r < ll)
    return false;
  if (rr < l) 
    return false;
  return true;
}

int main() {
  //assert(freopen("input.txt","r",stdin));
  //assert(freopen("output.txt","w",stdout));

  scanf("%d", &tn);

  for (int test = 1; test <= tn; test++) {
    scanf("%d %d", &n, &p);
    for (int i = 1; i <= n; i++) {
      scanf("%d", &need[i]);
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= p; j++) {
        scanf("%d", &a[i][j]);
      }
    }

    memset(from, -1, sizeof(from));
    memset(to, -1, sizeof(to));

    printf("Case #%d: ", test);

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= p; j++) {

        pair <int, int> r = rng(a[i][j], need[i]);
        from[i][j] = r.first; to[i][j] = r.second;
        //cout << from[i][j] << " " << to[i][j] << endl;

      }
      //cout << endl;
    }

    int ans = 0;
    if (n == 1) {
      for (int j = 1; j <= p; j++) {
        if (from[1][j] != -1) {
          ans++;
        }
      }
    }
    else {
      vector <int> v;
      for (int i = 1; i <= p; i++) {
        v.push_back(i);
      }
      do {
        int cur = 0;
        for (int i = 1; i <= p; i++) {
          if (cross(from[1][i], to[1][i], from[2][v[i - 1]], to[2][v[i - 1]])) {
            cur++;
          }
        }
        ans = max(ans, cur);
      } while (next_permutation(v.begin(), v.end()));
    }

    cout << ans << endl;
  }

  return 0;
}