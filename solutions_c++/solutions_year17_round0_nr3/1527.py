#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
typedef long long i64;

int T;
map<i64, i64> M;

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		i64 N, K;
		scanf("%lld%lld", &N, &K);
		M.clear();
		M.insert({ N, 1LL });

		i64 last;
		while (K > 0) {
			auto ls = *--M.end();
			M.erase(--M.end());

			last = ls.first;
			K -= ls.second;

			M[ls.first / 2] += ls.second;
			M[(ls.first - 1) / 2] += ls.second;
		}
		printf("Case #%d: %lld %lld\n", t, last / 2, (last - 1) / 2);
	}
	return 0;
}
