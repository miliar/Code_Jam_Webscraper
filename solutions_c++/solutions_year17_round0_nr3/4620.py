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
priority_queue <pair <int, int> > Q;
int main() {
   csl;
   cin >> t;
   for (int ii = 1; ii <= t; ++ii) {
      cout << "Case #" << ii << ": ";
      cin >> n >> k;
      Q = priority_queue <pair <int, int> > ();
      Q.push(make_pair(n, -n));
      for (int i = 1; i <= k; ++i) {
         pair <int, int> cur = Q.top();
         Q.pop();
         int r = -cur.second;
         int l = r - cur.first + 1;
         if ((r - l) % 2 == 0) {
            int x = (r + l) / 2;
            if (i == k) cout << r - x << " " << r - x;
            if (x != l) Q.push(make_pair(x - l, -(x - 1)));
            if (x != r) Q.push(make_pair(r - x, -r));
         } else {
            int x = (r + l) / 2;
            if (i == k) cout << r - x << " " << x - l;
            if (x != l) Q.push(make_pair(x - l, -(x - 1)));
            if (x != r) Q.push(make_pair(r - x, -r));
         }
      }
      cout << endl;
   }
   return 0;
}



















