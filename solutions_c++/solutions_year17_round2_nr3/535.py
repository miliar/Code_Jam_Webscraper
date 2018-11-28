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

const int N = 123;
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

int t, n, q, id;
ll d[N][N];
ld dist[N];
bool used[N];

struct horse {
  int e, s;
} a[N];

ld route(int start, int finish) {
  for (int i = 1;i <= n;i++) {
    dist[i] = 1e100;
    used[i] = 0;
  }
  dist[start] = 0.0;
  for (int it = 0;it < n;it++) {
    int v = -1;
    for (int i = 1;i <= n;i++) {
      if (used[i]) continue;
      if (v == -1 || dist[v] > dist[i]) {
        v = i;
      }
    }
    if (v == -1 || v == finish) break;
    used[v] = 1;
    for (int to = 1;to <= n;to++) {
      if (!used[to]) {
        if (a[v].e >= d[v][to]) {
          dist[to] = min(dist[to], dist[v] + 1.0 * d[v][to] / a[v].s);
        }
      }
    }
  }
  return dist[finish];
}
void solve() {
  id++;
  cin >> n >> q;
  for (int i = 1;i <= n;i++) cin >> a[i].e >> a[i].s;
  for (int i = 1;i <= n;i++) {
    for (int j = 1;j <= n;j++) {
      cin >> d[i][j];
      if (d[i][j] == -1) d[i][j] = Inf;
    }
  }
  //floyd
  for (int k = 1;k <= n;k++) {
    for (int i = 1;i <= n;i++) {
      for (int j = 1;j <= n;j++) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
      }
    }
  }
  cout << "Case #" << id << ": ";
  while(q--) {
    int start, finish;
    cin >> start >> finish;
    cout << fixed << setprecision(9) << route(start, finish) << " ";
  }
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