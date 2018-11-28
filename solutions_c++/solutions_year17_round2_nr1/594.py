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
int n;
double d, k, s;

int solve() {
  vector<pair<double, double>> a;
  cin >> d >> n;
  double sp, tt, md;
  double p = d, ans = 1e9, tmax = 0;
  for (int i = 0; i < n; ++i) {
    cin >> k >> s;
    // a.PB(MP(k, s));
    double t = (d-k)/s;
    if (t > tmax) {
      tmax = t;
      p = k;
    }
  }
  ans = d/tmax;
  // sp = a[n-1].SE, tt = (d-a[n-1].FI)/sp, md = d;
  // sort(ALL(a));
  // for (int i = n-1; i >= 0; --i) {
    // double t = (d - a[n-1].FI)/a[n-1].SE;
    // tmax = max(t, tmax);
  // }
  // ans = min(ans, d/t);
  // ans = d/tmax;

  printf("Case #%d: %.6lf\n", ti, ans);
  return 0;
}

int main() {
  cin >> T;
  for (ti = 1; ti <= T; ti++) {
    solve();
  }
  return 0;
}
