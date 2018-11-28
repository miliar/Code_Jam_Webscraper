#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <set>
#include <map>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <mmintrin.h>
#include <xmmintrin.h>
#include <emmintrin.h>

using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef pair<int, int> ipair;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A, B) make_pair(A,B)
const double pi = acos(-1.0);
#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define REP(i, a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T>
T sqr(const T& x) { return x * x; }

template<class T>
T lowbit(const T& x) { return (x ^ (x - 1)) & x; }

template<class T>
int countbit(const T& n) { return (n == 0) ? 0 : (1 + countbit(n & (n - 1))); }

template<class T>
void ckmin(T& a, const T& b) { if (b < a) a = b; }

template<class T>
void ckmax(T& a, const T& b) { if (b > a) a = b; }

const int maxn = 100000 + 16;

int n, d;
int a[maxn];
char s[maxn];

int solve() {
  int ret = 0;
  REP(i, n + 1) {
    if (a[i]) {
      if (i + d > n) return -1;
      ++ret;
      a[i + d] ^= 1;
    }
  }
  return ret;
}

int main() {
  //freopen("/home/acrush/helloworld/input.txt", "r", stdin);
  freopen("/home/acrush/helloworld/a2.in", "r", stdin);
  freopen("/home/acrush/helloworld/a2.out", "w", stdout);

  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    cin >> s >> d;
    n = strlen(s);
    s[n] = '+';
    memset(a, 0, sizeof(a));
    int p = 0;
    for (int i = 0; i <= n; ++i) {
      int w = (int)(s[i] == '-');
      if (w != p) a[i] = 1;
      p = w;
    }
    printf("Case #%d: ", case_id);
    int ret = solve();
    if (ret < 0)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", ret);
  }
  return 0;
}
