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
int N, R, O, Y, G, B, V;
string co = "ROYGBV";

int solve() {
  cin >> N;
  vector<pair<int, char>> v;
  for (int i = 0; i < 6; ++i) {
    int t;
    cin >> t;
    if (i%2 == 0)
      v.PB(MP(t, co[i]));
    // cout << t << ' ' << co[i] << endl;
  }
  sort(ALL(v));
  if (v[0].FI > v[1].FI+v[2].FI) {
    printf("Case #%d: IMPOSSIBLE\n", ti);
    return 0;
  }
  string ans;
  // int p = v[1].FI - v[0].FI;
  for (int i = 0; i < N; ++i) {
    if (v[2].FI > 0) {
      ans += v[2].SE;
      v[2].FI--;
    }
    if (v[1].FI + v[2].FI == 0)
      break;
    if (v[1].FI > v[0].FI) {
      ans += v[1].SE;
      v[1].FI--;
    } else {
      ans += v[0].SE;
      v[0].FI--;
    }
  }
  for (int i = 0; i < N; ++i)
    if ((int)ans.size() != N || (N > 1 && ans[i] == ans[(i+1)%N])) {
      printf("Case #%d: IMPOSSIBLE\n", ti);
      return 0;
    }


  printf("Case #%d: ", ti);
  cout << ans << endl;
  return 0;
}

int main() {
  cin >> T;
  for (ti = 1; ti <= T; ti++) {
    solve();
  }
  return 0;
}
