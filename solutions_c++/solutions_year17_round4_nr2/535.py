#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;
typedef long double ld;

const int MAX = 1005;
int takes[MAX];
int pos[MAX];

int T, n, c, m, a, b;

int solve(int rides) {
  int free = 0;
  int promo = 0;
  for (int i = 1; i <= n; i++) {
    free += rides;
    if (pos[i] > free) return -1;
    free -= pos[i];
    if (pos[i] > rides) promo += pos[i] - rides;
  }
  return promo;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out12.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  cin >> T;

  for (int tt = 1; tt <= T; tt++) {
    memset(takes, 0, sizeof takes);
    memset(pos, 0, sizeof pos);
    cin >> n >> c >> m;
    int minRides = 0;
    for (int i = 0; i < m; i++) {
      cin >> a >> b;
      takes[b]++;
      pos[a]++;
      minRides = max(minRides, takes[b]);
    }

    int l = minRides, h = m;
    int mid, best;
    int prom = -1;
    while(l <= h) {
      int mid = (l + h) / 2;
      int minPromotions = solve(mid);
      if (minPromotions != -1) {
        best = mid;
        prom = minPromotions;
        h = mid - 1;
      } else {
        l = mid + 1;
      }
    }


    cout << "Case #" << tt << ": ";
    cout << best << " " << prom << endl;

  }

  return 0;
}
