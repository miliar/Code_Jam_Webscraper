#include <map>
#include <cstdio>
#include <algorithm>
using namespace std;
#define long long long
#define pair pair<long, long>
int T;
long n, k;
map<long, long> *m;
int main() {
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++kase) {
		scanf("%lld%lld", &n, &k);
		m = new map<long, long>;
		(*m)[n] = 1;
		--k;
		while (k > 0) {
			pair top = *(m->rbegin());
			long u = top.first - 1, t = min(top.second, k);
			(*m)[u + 1] -= t;
			if (!(*m)[u + 1]) m->erase(u + 1);
			long v = u >> 1, w = u - v;
			(*m)[v] += t, (*m)[w] += t;
			k -= t;
		}
		long ans = m->rbegin()->first - 1;
		printf("Case #%d: %lld %lld\n", kase, ans - (ans >> 1), ans >> 1);
		delete m;
	}
	return 0;
}
