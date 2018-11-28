
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
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

int N, K;
uint64_t R[1001], H[1001];

struct PCake {
	uint64_t r;
	uint64_t h;
	uint64_t rh2;
	uint64_t r2;
};

PCake pcake[1001];

double Solve() {
 
	for (int i = 0; i < N; i++)
	{
		pcake[i].r = R[i];
		pcake[i].h = H[i];
		pcake[i].rh2 = 2 * R[i] * H[i];
		pcake[i].r2 = R[i] * R[i];
	}

	std::sort(&pcake[0], &pcake[N], [](const PCake &a, const PCake &b) { return a.rh2 > b.rh2; });
	
	uint64_t pk = 0;
	for (int i = 0; i < K; i++)
	{
		if (pk < pcake[i].r2)
			pk = pcake[i].r2;
	}

	uint64_t max_p_side = pk + pcake[K - 1].rh2;
	for (int i = K; i < N; i++)
	{
		if (pcake[i].r2 >= pk)
		{
			if (pcake[i].r2 + pcake[i].rh2 > max_p_side)
				max_p_side = pcake[i].r2 + pcake[i].rh2;
		}
	}

	uint64_t ans = 0;
	for (int i = 0; i < K - 1; i++)
	{
		ans += pcake[i].rh2;
	}

	ans += max_p_side;

    

	return 3.14159265359 * ans;
}

int main() {
  char buf[1024];
  fgets(buf, 1024, stdin);
  int T = atoi(buf);
  For(tcase, 1, T) {
    scanf("%d %d", &N, &K);
	for (int i = 0; i < N; i++)
		scanf("%lld %lld", &R[i], &H[i]);

    auto ans = Solve();

    printf("Case #%d: %.8f", tcase, ans);
    printf("\n");
  }
}
