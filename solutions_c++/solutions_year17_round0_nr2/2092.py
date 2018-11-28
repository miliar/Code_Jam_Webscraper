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

int t, id;
vector < int > ans, v;
ll n;

bool ok(int x) {
  int lst = inf;
  while(x) {
    if (x % 10 > lst) return 0;
    lst = x % 10;
    x /= 10;
  }
  return 1;
}
vector < int > slow(vector < int > v) {
  ll n = 0;
  for (auto i : v) n = n * 10 + i;
  ll ans = 0;
  for (int i = 1;i <= n;i++) {
    if (ok(i)) ans = i;
  }
  vector < int > res;
  while(ans) {
    res.pb(ans % 10);
    ans /= 10;
  }
  reverse(res.begin(), res.end());
  return res;
}

void solve() {
  id++;
  cin >> n;
  ans.clear();
  v.clear();
  while(n) {
    v.pb(n % 10);
    n /= 10;
  }
  ans.resize(v.size());
  reverse(v.begin(), v.end());
 // for (auto i : v) cout << i;
 // cout << endl;
  int mn = 0;
  for (int i = 0;i < v.size();i++) {
    if (v[i] < mn) {
      int ptr = i - 1;
      while(ptr > 0 && v[ptr - 1] == v[i - 1]) ptr--;
      ans[ptr]--;
      for (int j = ptr + 1;j < v.size();j++) ans[j] = 9;
      break;
    } else {
      ans[i] = v[i];
      mn = v[i];
    }
  }
  reverse(ans.begin(), ans.end());
  while(ans.size() && ans.back() == 0) ans.pp();
  reverse(ans.begin(), ans.end());
  cout << "Case #" << id << ": ";
  bool ok = 0;
  for (auto i : ans) cout << i;
  cout << endl;
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