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
const int N = 100;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 57;

long long arr[N];
string str, ss;

char f[N][N];
int can[N][N];
bool destroyed[N][N];
int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ": ";
      int r, c;
      cin >> r >> c;
      memset(can, 0, sizeof(can));
      memset(destroyed, 0, sizeof(destroyed));
      for (int i = 1; i <= r; ++i)
         for (int j = 1; j <= c; ++j) cin >> f[i][j];
      for (int i = 1; i <= r; ++i) {
         int last = -1;
         for (int j = 1; j <= c; ++j) {
            if (f[i][j] == '#') last = -1;
            else if (f[i][j] == '|' || f[i][j] == '-') {
               if (last == -1) last = j;
               else {
                  can[i][last] |= 1;
                  can[i][j] |= 1;
                  last = j;
               }
            }
         }
      }
      for (int j = 1; j <= c; ++j) {
         int last = -1;
         for (int i = 1; i <= r; ++i) {
            if (f[i][j] == '#') last = -1;
            else if (f[i][j] == '|' || f[i][j] == '-') {
               if (last == -1) last = i;
               else {
                  can[last][j] |= 2;
                  can[i][j] |= 2;
                  last = i;
               }
            }
         }
      }
      bool valid = true;
      for (int i = 1; i <= r; ++i)
         for (int j = 1; j <= c; ++j)
            if (can[i][j] == 3) {
               valid = false;
            } else {
               if (f[i][j] == '#' || f[i][j] == '.')
                  continue;
               if (can[i][j] == 0 || can[i][j] == 2) f[i][j] = '-';
               else f[i][j] = '|';
            }
      for (int i = 1; i <= r; ++i) {
         for (int j = 1; j <= c; ++j) {
            if (f[i][j] == '-') {
               for (int k = j + 1; k <= c && f[i][k] != '#'; ++k) {
                  destroyed[i][k] = true;
               }
               for (int k = j - 1; k >= 1 && f[i][k] != '#'; --k) {
                  destroyed[i][k] = true;
               }
            } else if (f[i][j] == '|') {
               for (int k = i + 1; k <= r && f[k][j] != '#'; ++k) {
                  destroyed[k][j] = true;
               }
               for (int k = i - 1; k >= 1 && f[k][j] != '#'; --k) {
                  destroyed[k][j] = true;
               }
            }
         }
      }
      for (int i = 1; i <= r; ++i) {
         for (int j = 1; j <= c; ++j) {
            if (f[i][j] == '.' && destroyed[i][j] == false) {
               for (int k = i + 1; k <= r && f[k][j] != '#'; ++k) {
                  if (f[k][j] == '-' && can[k][j] == 0) {
                     f[k][j] = '|';
                  }
               }
               for (int k = i - 1; k >= 1 && f[k][j] != '#'; --k) {
                  if (f[k][j] == '-' && can[k][j] == 0) {
                     f[k][j] = '|';
                  }
               }

            }
         }
      }
      memset(destroyed, 0, sizeof(destroyed));
      for (int i = 1; i <= r; ++i) {
         for (int j = 1; j <= c; ++j) {
            if (f[i][j] == '-') {
               for (int k = j + 1; k <= c && f[i][k] != '#'; ++k) {
                  destroyed[i][k] = true;
               }
               for (int k = j - 1; k >= 1 && f[i][k] != '#'; --k) {
                  destroyed[i][k] = true;
               }
            } else if (f[i][j] == '|') {
               for (int k = i + 1; k <= r && f[k][j] != '#'; ++k) {
                  destroyed[k][j] = true;
               }
               for (int k = i - 1; k >= 1 && f[k][j] != '#'; --k) {
                  destroyed[k][j] = true;
               }
            }
         }
      }
      for (int i = 1; i <= r; ++i) {
         for (int j = 1; j <= c; ++j) {
            if (f[i][j] == '.' && destroyed[i][j] == false) valid = false;
         }
      }
      if (!valid) cout << "IMPOSSIBLE" << endl;
      else {
         cout << "POSSIBLE" << endl;
         for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j)
               cout << f[i][j];
            cout << endl;
         }
      }
   }
   return 0;
}





















