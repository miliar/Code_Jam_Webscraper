// CONTEST SOURCE
#include <algorithm>
#include <climits>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define VI vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define pi 2 * acos(0.)
int t, n, d;
pair<int, int> a[1111];
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    scanf("%d%d", &d, &n);
    for(int i = 0; i < n; ++i) scanf("%d%d", &a[i].x, &a[i].y);
    double ub = 1e20;
    for(int i = 0; i < n; ++i) {
      ub = min(ub, (1. * d) * a[i].y * 1. / (d - a[i].x));
    }
    printf("Case #%d: %0.9lf\n", tc, ub);
  }
}
