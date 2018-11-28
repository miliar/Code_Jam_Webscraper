#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

template<typename T>
void PRINT(T a) {cerr<<a<<endl;}
template<typename T>
void PRINT(vector<T> &a) {for(auto i:a)cerr<<i<<" ";cerr<<endl;}
template<typename T>
void PRINT(vector<vector<T>> &a) {for(auto i: a)PRINT(i);}
template<typename T>
void PRINT(T *a, int n) {for(int i=0;i<n;++i)cerr<<a[i]<<' ';cerr<<endl;}

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef pair<int, string> PIS;
typedef pair<LL, LL> PLL;
typedef pair<double, double> PDD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<bool> VB;
typedef vector<vector<int>> VVI;
typedef vector<vector<bool>> VVB;
typedef vector<vector<double>> VVD;
typedef unordered_set<int> SI;
typedef unordered_set<double> SD;
typedef unordered_map<int, int> MII;
typedef unordered_map<string, int> MSI;
typedef unordered_map<double, int> MDI;

#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) (int((x).size()))

// =================================

int T, ti;
int u[20], l[20], mp[20][20], r[20], a[2][20];
int n, p, tt;

int check(int i, int j) {
  int x1 = ceil(a[0][i]/(1.1*r[0]));
  int y1 = floor(a[0][i]/(0.9*r[0]));
  int x2 = ceil(a[1][j]/(1.1*r[1]));
  int y2 = floor(a[1][j]/(0.9*r[1]));
  // cout << i << '#' << j << " | " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
  return (y1 > 0 && y2 > 0 && !(y2 < x1 || y1 < x2));
}

  int can(int t) {
    for (int i = 0; i < p; ++i)
      if (u[i] == 0 && mp[t][i]) {
        u[i] = 1;
        if (l[i] == -1 || can(l[i])) {
          l[i] = t;
          return 1;
        }
      }
    return 0;
  }

int solve() {
  cin >> n >> p;
  // cout << n << endl;
  for (int i = 0; i < n; ++i)
    cin >> r[i];
  if (n == 1) {
    int ans = 0;
    for (int i = 0; i < p; ++i) {
      cin >> tt;
      int x1 = ceil(tt/(1.1*r[0]));
      int y1 = floor(tt/(0.9*r[0]));
      if (y1 >= x1 && y1 > 0)
        ++ans;
    }
    printf("Case #%d: %d\n", ti, ans);
    return 0;
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < p; ++j)
      cin >> a[i][j];
  }
  for (int i = 0; i < p; ++i) {
    for (int j = 0; j < p; ++j) {
      mp[i][j] = check(i, j);
      // cout << mp[i][j] << ' ';
    }
    // cout << '/' << endl;
  }
  int ans = 0;
  memset(l, 0xff, sizeof(l));
  for (int i = 0; i < p; ++i) {
    memset(u, 0, sizeof(u));
    if (can(i)) ++ans;
  }

  printf("Case #%d: %d\n", ti, ans);
  return 0;
}

int main() {
  cin >> T;
  for (ti = 1; ti <= T; ti++) {
    solve();
  }
  return 0;
}
