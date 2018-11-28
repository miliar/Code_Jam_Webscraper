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
int has[100][100];
int R[N];
int pos[N];
int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ": ";
      int p;
      cin >> n >> p;
      for (int i = 1; i <= n; ++i) cin >> R[i];
      for (int i = 1; i <= n; ++i) {
         for (int j = 1; j <= p; ++j) cin >> has[i][j];
         sort(has[i] + 1, has[i] + 1 + p);
      }
      int res = 0;
      for (int iter = 1; iter <= 1e6; ++iter) {
         int sz = 0;
         if (p == 0) break;
         for (int i = 1; i <= n; ++i) {
            int lo = 1, hi = p;
            while (lo < hi) {
               int mid = (lo + hi) / 2;
               if (has[i][mid] * 100 >= 1LL * 90 * iter * R[i]) hi = mid;
               else lo = mid + 1;
            }
            if ((has[i][lo] * 100 >= 1LL * 90 * iter * R[i]) && (has[i][lo] * 100 <= 1LL * R[i] * 110 * iter)) pos[sz++] = lo;
            else break;
         }
         if (sz < n) continue;
         res++;
         //cout << iter << " ";
         for (int i = 1; i <= n; ++i) {
           // cout << pos[i - 1] << " ";
            swap(has[i][pos[i - 1]], has[i][p]);
            if (p > 1) sort(has[i] + 1, has[i] + p);
         }
         //cout << endl;
         iter--;
         p--;
      }
      cout << res;
      cout << '\n';
   }
   return 0;
}


















