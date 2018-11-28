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
#include <queue>

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

const int N = 1e5 + 123;
const int MM = 1e6;
const ld Pi = acos(-1);
const ll Inf = 1e18;
const int inf = 1e9 + 123;
const int mod = 1e9 + 7;
const ld eps = 1e-9;
const int Sz = 1;

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

int t, n, k, a[N], id;
string s;

void solve() {
  id++;
  cin >> s >> k;
  n = s.size();
  for (int i = 0;i < n;i++) a[i] = (s[i] == '+');
  int ans = 0;
  for (int i = 0;i + k - 1 < n;i++) {
    if (!a[i]) {
      ans++;
      for (int j = 0;j < k;j++) a[i + j] ^= 1;
    }
  }
  bool fail = 0;
  for (int i = 0;i < n;i++) if (!a[i]) fail = 1;
  cout << "Case #" << id << ": ";
  if (fail) cout << "IMPOSSIBLE\n";
  else cout << ans << "\n";
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