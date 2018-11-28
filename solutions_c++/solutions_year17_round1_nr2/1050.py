#pragma comment(linker, "/STACK:134217728") //128mb
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cassert>
#include <climits>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <hash_set>
#include <hash_map>
#include <unordered_set>
#include <algorithm>
#include <random>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <complex>
using namespace std;


#define input_txt freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define in_out(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define all(x) x.begin(),x.end()

typedef long long ll;
typedef long long llong;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef complex<double> comp;

const long long MOD = 1000000000 + 7; //1e9+7
const long long MAXN = 100000 + 100; //1e5
const long long MAGIC = 123123123;
const double PI = 4 * atan(1.);
const double EPS = 1E-7;
const int LOGN = 22;



struct cmp_for_set {
  bool operator()(const int & a, const int & b){ return a > b; }
};

void time_elapsed() { cout << "\nTIME ELAPSED: " << (double)clock() / CLOCKS_PER_SEC << " sec\n"; }
#define DOUT_VAR(x) cout << #x << " = " << (x) << endl
template<typename T> void DOUT_VEC(vector<T> & vec) { puts("");  for (auto i : vec) cout << i << " "; puts(""); }
template<typename T> void DOUT_TABLE(vector<vector<T>> & vec) { puts(""); for (auto i : vec) { for (auto j : i) cout << j << " "; cout << endl; }puts(""); }

template<typename T> T gcd(T a, T b){ return ((!b) ? a : gcd(b, a%b)); }
template<typename T>T gcd(T a, T b, T&x, T&y){ if (!a){ x = 0, y = 1; return b; }T x1, y1; T d = gcd(b%a, a, x1, y1); x = y1 - (b / a)*x1; y = x1; return d; }

template<typename T> T lcm(T a, T b) { return (a / gcd(a, b))*b; }
template<typename T, typename M> T neg_mod(T a, M mod) { return ((a%mod) + mod) % mod; }
ll binpow(ll x, ll p) { ll res = 1; while (p){ if (p & 1) res *= x; x *= x; p >>= 1; }return res; }
ll binpow_mod(ll x, ll p, ll m) { ll res = 1; while (p){ if (p & 1) res = (res*x) % m; x = (x*x) % m; p >>= 1; }return res; }

int dp[1 << 16];

int bitcnt(int v) {
  int res = 0;
  while (v) {
    res += (v & 1);
    v >>= 1;
  }
  return res;
}

bool intersect(int a, int b, int c, int d) {
  if (a > b || c > d)return false;
  if (a > c) return intersect(c, d, a, b);
  return c >= a && c <= b;
}

int main() {
  input_txt;

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n, p;
    cin >> n >> p;
    vector<int>r(n);
    for (int i = 0; i < n; ++i) {
      cin >> r[i];
    }
    vector<vector<int>>q(n, vector<int>(p));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> q[i][j];
      }
    }
    
    memset(dp, 0, sizeof(dp));

    vector<int>cur(n);
    int res = 0;
    for (int mask = 0; mask < (1 << (n*p)); ++mask) {
      for (int sub = mask; sub; sub = (mask & (sub - 1))) {
        if (bitcnt(sub) != n) continue;
        for (int i = 0; i < n; ++i) {
          cur[i] = -1;
          for (int j = 0; j < p; ++j) {
            if (sub & (1 << (p*i + j))) {
              cur[i] = q[i][j];
            }
          }
        }
        bool bad = false;
        for (int i = 0; i < n; ++i) {
          if (cur[i] == -1) bad = true;
        }
        if (bad)continue;
        if (n == 1) {
          if ((10 * cur[0] + 11 * r[0] - 1) / (11 * r[0])<=
            (10 * cur[0]) / (9 * r[0]))
          dp[mask] = max(dp[mask], dp[mask ^ sub]+1);
        }
        else {
          if (intersect(
            (10 * cur[0] + 11 * r[0] - 1) / (11 * r[0]),
            (10 * cur[0]) / (9 * r[0]),
            (10 * cur[1] + 11 * r[1] - 1) / (11 * r[1]),
            (10 * cur[1]) / (9 * r[1]))) {
            dp[mask] = max(dp[mask], 1+dp[mask^sub]);
          }
        }
      }
      res = max(res, dp[mask]);
    }
    printf("Case #%d: %d\n", test, res);
  }

  //time_elapsed();
  return 0;
}