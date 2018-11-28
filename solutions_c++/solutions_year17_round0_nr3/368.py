#include <cstdio>
#include <map>
using namespace std;

typedef long long i64;

int T;

int main() {
	freopen("C.in", "r", stdin);
	scanf("%d", &T);

	for (int id = 1; id <= T; ++id) {
		map<i64, i64> cnt;
		i64 n, m;
		scanf("%lld%lld", &n, &m);
		cnt[n] = 1;

		for (auto it = cnt.rbegin(); it != cnt.rend(); ++it) {
			i64 t = it->first;
			m -= it->second;
			i64 t0 = t / 2, t1 = (t - 1) / 2;
			if (m <= 0) {
				printf("Case #%d: %lld %lld\n", id, t0, t1);
				break;
			}
			cnt[t0] += it->second;
			cnt[t1] += it->second;
		}
	}
	return 0;
}