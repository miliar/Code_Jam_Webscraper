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
string str, ss;
int rem[N];
int dp[105][105][105][4];
long long P;
int solve(int ra, int rb, int rc, int p) {
   if (ra + rb + rc == 0) return 0;
   if (dp[ra][rb][rc][p] != -1) return dp[ra][rb][rc][p];
   int &ret = dp[ra][rb][rc][p];
   ret = 0;
   if (ra != 0) {
      ret = max(ret, solve(ra - 1, rb, rc, (p - 1 + P) % P));
   }
   if (rb != 0) {
      ret = max(ret, solve(ra, rb - 1, rc, (p - 2 + P) % P));
   }
   if (rc != 0) {
      ret = max(ret, solve(ra, rb, rc - 1, (p - 3 + P) % P));
   }
   if (p == 0) ret++;
   return ret;
}
int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ": ";
      memset(dp, -1, sizeof(dp));
      memset(rem, 0, sizeof(rem));
      cin >> n >> P;
      for (int i = 1; i <= n; ++i) cin >> arr[i];
      for (int i = 1; i <= n; ++i)
         rem[arr[i] % P]++;
      long long ans = rem[0];
      cout << ans + solve(rem[1], rem[2], rem[3], 0) << '\n';
   }
   return 0;
}





















