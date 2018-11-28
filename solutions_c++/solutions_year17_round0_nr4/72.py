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

const int maxsize = 1024;

int a[maxsize][maxsize];
int sx[maxsize], sy[maxsize], ss[maxsize], sd[maxsize];
int o[maxsize][maxsize];

int main() {
  //freopen("/home/acrush/helloworld/input.txt", "r", stdin);
  freopen("/home/acrush/helloworld/d2.in", "r", stdin);
  freopen("/home/acrush/helloworld/d2.out", "w", stdout);

  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    printf("Case #%d: ", case_id);
    int n, m;
    cin >> n >> m;
    memset(a, 0, sizeof(a));
    REP(i, m) {
      char s[8];
      int x, y;
      cin >> s >> x >> y;
      --x;
      --y;
      if (s[0] == 'x') a[x][y] = 1;
      if (s[0] == '+') a[x][y] = 2;
      if (s[0] == 'o') a[x][y] = 3;
    }
    memcpy(o, a, sizeof(a));
    memset(sx, 0, sizeof(sx));
    memset(sy, 0, sizeof(sy));
    memset(ss, 0, sizeof(ss));
    memset(sd, 0, sizeof(sd));
    REP(x, n) {
      REP(y, n) {
        if (a[x][y] & 1) {
          ++sx[x];
          ++sy[y];
        }
        if (a[x][y] & 2) {
          ++ss[x + y];
          ++sd[x + n - y];
        }
      }
    }
    REP(x, n) {
      REP(y, n) {
        if (!(a[x][y] & 1) && !sx[x] && !sy[y]) {
          a[x][y] |= 1;
          ++sx[x];
          ++sy[y];
        }
      }
    }
    for (int abs_s = n - 1; abs_s >= 0; --abs_s) {
      REP(op, 2) {
        int s = n - 1 + (op ? abs_s : -abs_s);
        for (int x = max(0, s - n + 1); x <= min(n - 1, s); ++x) {
          int y = s - x;
          if (!(a[x][y] & 2) && !ss[x + y] && !sd[x + n - y]) {
            a[x][y] |= 2;
            ++ss[x + y];
            ++sd[x + n - y];
          }
        }
      }
    }
    int r1 = 0, r2 = 0;
    REP(x, n) {
      REP(y, n) {
        if (a[x][y] & 1) ++r1;
        if (a[x][y] & 2) ++r1;
        if (a[x][y] != o[x][y]) ++r2;
      }
    }
    printf("%d %d\n", r1, r2);
    REP(x, n) {
      REP(y, n) {
        if (a[x][y] != o[x][y]) {
          char c;
          if (a[x][y] == 1) c = 'x';
          if (a[x][y] == 2) c = '+';
          if (a[x][y] == 3) c = 'o';
          printf("%c %d %d\n", c, x + 1, y + 1);
        }
      }
    }
  }
  return 0;
}
