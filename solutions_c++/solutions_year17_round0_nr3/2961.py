
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef long double ld;

#define For(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define Ford(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define Rep(i, n) for (int i(0), _n(n); i < _n; ++i)
#define Repd(i, n) for (int i((n)-1); i >= 0; --i)
#define Fill(a, c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define Max(a, b) (a) < (b) ? (b) : (a)
#define Min(a, b) (a) < (b) ? (a) : (b)

template <typename T, typename S> T cast(S s) {
  stringstream ss;
  ss << s;
  T res;
  ss >> res;
  return res;
}

template <typename T> inline T sqr(T a) { return a * a; }
template <typename T> inline int Size(const T &c) { return (int)c.size(); }
template <typename T> inline void checkMin(T &a, T b) {
  if (b < a)
    a = b;
}
template <typename T> inline void checkMax(T &a, T b) {
  if (b > a)
    a = b;
}

int64_t N;
int64_t K;
int64_t ans_max, ans_min;

int Solve() {
	int64_t l1, l2;
	l1 = 0;
	l2 = 1;
	while (l2 < K) {
		l1 = l2;
		l2 = l2 * 2 + 1;
	}
	// assert l1 < K <= l2

	int64_t d = (N - l1) / (l1+1);
	int64_t r = (N - l1) % (l1+1);
	int64_t max_seg;
	if (K - l1 <= r)
		max_seg = d + 1;
	else
		max_seg = d;

	ans_min = (max_seg - 1) / 2;
	ans_max = (max_seg - 1) - ans_min;

  return 0;
}

int main() {
  char buf[1024];
  fgets(buf, 1024, stdin);
  int T = atoi(buf);
  For(tcase, 1, T) {
    scanf("%lld %lld", &N, &K);

    auto ans = Solve();

    printf("Case #%d: %lld %lld", tcase, ans_max, ans_min);
    printf("\n");
  }
}
