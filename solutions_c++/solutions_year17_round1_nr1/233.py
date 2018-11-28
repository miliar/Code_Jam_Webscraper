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

int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ":\n";
      int R, C;
      cin >> R >> C;
      for (int i = 1; i <= R; ++i) {
         cin >> str[i];
         for (int j = 1; j < str[i].size(); ++j) {
            if (str[i][j] == '?') str[i][j] = str[i][j - 1];
         }
         for (int j = (int)str[i].size() - 2; j >= 0; --j) {
            if (str[i][j] == '?') str[i][j] = str[i][j + 1];
         }
      }
      for (int i = 2; i <= R; ++i) {
         for (int j = 0; j < str[i].size(); ++j) {
            if (str[i][j] == '?') str[i][j] = str[i - 1][j];
         }
      }
      for (int i = R - 1; i >= 1; --i) {
         for (int j = 0; j < C; ++j) {
            if (str[i][j] == '?') str[i][j] = str[i + 1][j];
         }
      }
      for (int i = 1; i <= R; ++i) {
         for (int j = 0; j < C; ++j) cout << str[i][j];
         cout << '\n';
      }
      cout << '\n';
   }
   return 0;
}


















