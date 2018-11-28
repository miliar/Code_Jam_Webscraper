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

int main() {
  //freopen("/home/acrush/helloworld/input.txt", "r", stdin);
  freopen("/home/acrush/helloworld/c3.in", "r", stdin);
  freopen("/home/acrush/helloworld/c3.out", "w", stdout);

  int64 ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    cout << "Case #" << case_id << ": ";
    map<int64, int64> w;
    int64 n, k;
    cin >> n >> k;
    ++w[n];
    while (1) {
      auto t = *(--w.end());
      w.erase(--w.end());
      int64 length = t.first;
      int64 cnt = t.second;
      int64 l1 = (length - 1) / 2;
      int64 l2 = length - 1 - l1;
      if (cnt >= k) {
        cout << l2 << " " << l1 << endl;
        break;
      }
      k -= cnt;
      w[l1] += cnt;
      w[l2] += cnt;
    }
  }
  return 0;
}
