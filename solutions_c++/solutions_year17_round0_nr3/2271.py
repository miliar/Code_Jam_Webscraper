#include <stdio.h>
#include <map>

int main() {
	long long T, N, K, n, c, t = 1; std::map<long long, long long> m; std::map<long long, long long>::iterator it;
	for (scanf("%lld", &T); T--; printf("Case #%lld: %lld %lld\n", t++, n/2, n%2 ? n/2 : n/2-1))
		for (scanf("%lld%lld", &N, &K), m.clear(), m[N]++; K > 0; )
			n = (--(it = m.end()))->first, c = it->second, n%2 ? (m[n/2] += 2*c) : (m[n/2] += c, m[n/2-1] += c), K -= c, m.erase(it);
}
