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

const int N = 1e5 + 123;
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

int t, n, a[6], id, ans[N], b[N];
string ch = "ROYGBV";

string go(int start) {
  for (int i = 0;i < 6;i++) b[i] = a[i];
  ans[0] = start;
  b[start]--;
  for (int i = 1;i < n;i++) ans[i] = -1;
  string str = "";
  str += ch[start];
  for (int i = 1;i < n;i++) {
    int x = ans[(i + n - 1) % n];
    int y = ans[(i + 1) % n];
    int mx = 0, cur = -1;
    for (int j = 0;j < 6;j++) {
      if (x == j || y == j) continue;
      if (b[j] > 0 && mx < b[j]) {
        mx = b[j];
        cur = j;
      }
    }
    if (cur == -1) return str = "IMPOSSIBLE";
    str += ch[cur];
    ans[i] = cur;
    b[cur]--;
  }
  return str;
}
void Error() { 
  cout << "Error\n";
  cout << n << " ";
  for (int i = 0;i < 6;i++) cout << a[i] << " ";
  cout << endl;
  assert(0);
  exit(0);
}
void solve() {
  id++;
  cin >> n;
  int x = 0;
  for (int i = 0;i < 6;i++) {
    cin >> a[i];
    x = max(x, a[i]);
    if (i & 1) assert(a[i] == 0);
  }
  cout << "Case #" << id << ": ";
  string now = "IMPOSSIBLE";
  for (int i = 0;i < 6;i++) {
    if (a[i]) {
      now = go(i);
      if (now != "IMPOSSIBLE") break;
    }
  }
  if (x <= n / 2 && now == "IMPOSSIBLE") {
    Error();
  }
  cout << now << endl;
  if (now == "IMPOSSIBLE") return;
  assert(now.size() == n);
  if (now.size() != n) {
    cout << now << endl;
    Error();
  }
  for (int i = 0;i < n;i++) {
    auto x = now[(i + 1) % n];
    auto y = now[(i + n - 1) % n];
    if (x == now[i] || now[i] == y) {
      Error();
    }
  }
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