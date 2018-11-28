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
int N, Q;
int E[200], S[200];
double D[200][200]; // , d[200][200];
double t[200];
int u, v;

int solve() {
  cin >> N >> Q;
  for (int i = 0; i < N; ++i) {
    cin >> E[i] >> S[i];
    t[i] = 1e20;
  }
  vector<vector<double>> d(N, vector<double>(N));
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j) {
      cin >> D[i][j];
      d[i][j] = D[i][j];
    }
  // PRINT(d);
  for (int k = 0; k < N; ++k)
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j) {
        if (i != j && d[i][k] != -1 && d[k][j] != -1) {
          if (d[i][j] == -1) {
            d[i][j] = d[i][k] + d[k][j];
          } else {
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
          }
        }
      }
  // if (ti == 11)
    // PRINT(d);
  vector<vector<int>> ne(N, vector<int>{});
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      if (d[i][j] > 0)
        ne[i].PB(j);

  printf("Case #%d:", ti);
  for (int qi = 0; qi < Q; ++qi) {
    cin >> u >> v;
    --u, --v;
    vector<double> t(N, 1e20);
    vector<int> bbb(N);
    t[u] = 0;
    queue<int> q;
    q.push(u);
    // cout << '#' << S[0] << endl;
    bbb[u] = 1;
    while (!q.empty()) {
      int ss = q.front();
      q.pop();
      --bbb[ss];
      for (int ij = 0; ij < (int)ne[ss].size(); ++ij) {
        int j = ne[ss][ij];
        if (d[ss][j] > 0 && d[ss][j] <= E[ss] && t[ss]+d[ss][j]*1.0/S[ss] < t[j]) {
          t[j] = t[ss]+d[ss][j]*1.0/S[ss];
          if (bbb[j] == 0) {
            q.push(j);
            bbb[j]++;
          }
        }
      }
    }
    printf(" %.9lf", t[v]);
  }
  cout << endl;

  return 0;
}

int main() {
  cin >> T;
  for (ti = 1; ti <= T; ti++) {
    solve();
  }
  return 0;
}
