#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector <long long> vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector <int> vii;
typedef complex <double> Point;

#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second

long long t, n, m, u, v, q, k;
const int N = 2e5 + 500;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 57;

long long arr[N];
string str[N], ss;
int was[102][102][102][102];
int R[N];
int pos[N];
queue <pair <pair <int, int>, pair<int, int> > > Q;
int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ": ";
      memset(was, -1, sizeof(was));
      int hd, ad, hk, ak, b, d;
      int mhd, mad, mhk, mak, mb, md;
      cin >> hd >> ad >> hk >> ak >> b >> d;
      mhd = hd, mad = ad, mhk = hk, mak = ak, mb = b, md = d;
      was[hd][ad][hk][ak] = 0;
      Q = queue <pair <pair <int, int>, pair<int, int> > > ();
      Q.push(make_pair(make_pair(hd, ad), make_pair(hk, ak)));
      int sol = INT_MAX;
      while (Q.size() > 0) {
         pair <pair <int, int>, pair <int, int> > v = Q.front();
         Q.pop();
         if (v.first.first == 0) continue;
         if (v.second.first == 0) {
            sol = was[v.first.first][v.first.second][v.second.first][v.second.second];
            break;
         }
         pair <pair <int, int>, pair <int, int> > u;
         u = v;
         u.first.first = v.first.first - v.second.second;
         u.second.first = v.second.first - v.first.second;
         if (u.second.first <= 0) {
            u.second.first = 0;
            u.first.first += v.second.second;
         }
         if (u.first.first <= 0) u.first.first = 0;
         if (was[u.first.first][u.first.second][u.second.first][u.second.second] == -1) {
            was[u.first.first][u.first.second][u.second.first][u.second.second] = was[v.first.first][v.first.second][v.second.first][v.second.second] + 1;
            Q.push(u);
         }
         u = v;
         u.first.first = hd;
         u.first.first -= u.second.second;
         if (u.first.first <= 0) u.first.first = 0;
         if (was[u.first.first][u.first.second][u.second.first][u.second.second] == -1) {
            was[u.first.first][u.first.second][u.second.first][u.second.second] = was[v.first.first][v.first.second][v.second.first][v.second.second] + 1;
            Q.push(u);
         }
         u = v;
         u.first.second += b;
         u.first.first -= u.second.second;
         if (u.first.first <= 0) u.first.first = 0;
         if (was[u.first.first][u.first.second][u.second.first][u.second.second] == -1) {
            was[u.first.first][u.first.second][u.second.first][u.second.second] = was[v.first.first][v.first.second][v.second.first][v.second.second] + 1;
            Q.push(u);
         }
         u = v;
         u.second.second -= d;
         if (u.second.second <= 0) u.second.second = 0;
         u.first.first -= u.second.second;
         if (u.first.first <= 0) u.first.first = 0;
         if (was[u.first.first][u.first.second][u.second.first][u.second.second] == -1) {
            was[u.first.first][u.first.second][u.second.first][u.second.second] = was[v.first.first][v.first.second][v.second.first][v.second.second] + 1;
            Q.push(u);
         }
      }
      if (sol == INT_MAX) cout << "IMPOSSIBLE";
      else cout << sol;
      cout << endl;
   }
   return 0;
}


















