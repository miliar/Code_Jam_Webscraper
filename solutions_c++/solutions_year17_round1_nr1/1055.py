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




int main() {
  input_txt;

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n, m;
    cin >> n >> m;
    vector<string> vec(n);
    for (int i = 0; i < n; ++i) {
      cin >> vec[i];
    }
    for (int i = 0; i < n; ++i) {
      char prev = '$';
      for (int j = 0; j < m; ++j) {
        if (vec[i][j] != '?') {
          prev = vec[i][j];
        }
        else if (prev != '$') {
          vec[i][j] = prev;
        }
      }
    }
    for (int i = 0; i < n; ++i) {
      char prev = '$';
      for (int j = m-1; j >=0 ; --j) {
        if (vec[i][j] != '?') {
          prev = vec[i][j];
        }
        else if (prev != '$') {
          vec[i][j] = prev;
        }
      }
    }
    for (int i = 1; i < n; ++i) {
      for (int j = 0; j < m; ++j){
        if (vec[i][j] == '?') vec[i][j] = vec[i - 1][j];
      }
    }
    for (int i = n-2; i >=0; --i) {
      for (int j = 0; j < m; ++j){
        if (vec[i][j] == '?') vec[i][j] = vec[i + 1][j];
      }
    }

    printf("Case #%d:\n", test);
    for (int i = 0; i < n; ++i) {
      cout << vec[i] << endl;
    }
    
  }

  //time_elapsed();
  return 0;
}