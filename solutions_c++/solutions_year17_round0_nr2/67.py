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

int64 solve(int64 p10, int last, int64 current, int64 target) {
  int64 base = current;
  for (int64 w = p10; w > 0; w /= 10) base += w * last;
  if (base > target) return -1;
  if (p10 == 0) return current;
  for (int i = 9; i >= last; --i) {
    int64 t = solve(p10 / 10, i, current + p10 * i, target);
    if (t >= 0) return t;
  }
  return -1;
}

int main() {
  //freopen("/home/acrush/helloworld/input.txt", "r", stdin);
  freopen("/home/acrush/helloworld/b2.in", "r", stdin);
  freopen("/home/acrush/helloworld/b2.out", "w", stdout);

  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    printf("Case #%d: ", case_id);
    int64 n;
    cin >> n;
    int64 p10 = 1000000000LL * 1000000000LL;
    while (1) {
      int64 t = solve(p10, 1, 0, n);
      if (t >= 0) {
        printf("%lld\n", t);
        break;
      }
      p10 /= 10;
    }
  }
  return 0;
}
