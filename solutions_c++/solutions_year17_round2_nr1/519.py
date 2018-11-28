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

using namespace std;

#define f first
#define s second
#define pb push_back
#define pp pop_back
#define mp make_pair
#define ll long long
#define ld long double
#define ull unsigned long long
#define PI pair < int, int > 

const int N = 1e6 + 123;
const int M = 123;
const ld Pi = acos(-1);
const ll Inf = 1e18;
const int inf = 1e9;
const int mod = 1e9 + 7;
const int Sz = 350;

void add(int &a, int b) {
  a += b;
  if (a >= mod) a -= mod;
}
int mult(int a, int b) {
  return 1ll * a * b % mod;
}
int sum(int a, int b) {
  add(a, b);
  return a;
}

int t, n, id, d;

struct horse {
  int k, s;
} a[N];

bool check(ld x) {
  ld req = 1.0 * d / x; 
  for (int i = 1;i <= n;i++) {
    if (a[i].s >= x) continue;
    ld now = 1.0 * a[i].k / (x - a[i].s);
    if (req > now) return 0;
  }
  return 1;
}
void solve() {
  id++;
  cin >> d >> n;
  for (int i = 1;i <= n;i++) cin >> a[i].k >> a[i].s;
  ld l = 0.0, r = 1e18;
  for (int it = 0;it < 200;it++) {
    ld mid = (l + r) / 2.0;
    if (check(mid)) l = mid;
    else r = mid;
  }
  cout << "Case #" << id << ": " << fixed << setprecision(9) << l << endl;
}
int main() {
  #ifdef wws
    freopen("in", "r", stdin);
    freopen("out", "w", stdout); 
  #endif 
  ios_base::sync_with_stdio(0);
  cin >> t;
  while(t--) solve();
  return 0; 
}