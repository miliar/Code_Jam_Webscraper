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

int T, ti, n, k;
string s;

int solve() {
  cin >> s >> k;
  n = s.size();
  int i, ans = 0;
  for (i = 0; i <= n-k; ++i) {
    if (s[i] == '-') {
      for (int j = 0; j < k; ++j)
        s[j+i] = '-'+'+'-s[j+i];
      ++ans;
    }
  }
  for (i = n-k+1; i < n; ++i)
    if (s[i] == '-') {
      printf("Case #%d: IMPOSSIBLE\n", ti);
      return 0;
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
