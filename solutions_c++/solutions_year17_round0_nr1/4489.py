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

int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ": ";
      cin >> str >> k;
      int res = 0;
      for (int i = 0; i < str.size() - k + 1; ++i) {
         if (str[i] == '-') {
            res++;
            for (int j = i; j < i + k; ++j) {
               if (str[j] == '-') str[j] = '+';
               else str[j] = '-';
            }
         }
      }
      bool valid = true;
      for (int i = 0; i < str.size(); ++i) {
         if (str[i] == '-') valid = false;
      }
      if (valid) cout << res;
      else cout << "IMPOSSIBLE";
      cout << endl;
   }
   return 0;
}



















