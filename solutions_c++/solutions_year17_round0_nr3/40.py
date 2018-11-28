#include <bits/stdc++.h>
using namespace std;

int TC;
long long N, K;
map<long long, long long> M;

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%lld%lld", &N, &K);
		M.clear();
		M[N] = 1;
		while (1) {
			pair<long long, long long> P = *M.rbegin();
			M.erase(--M.end());
			long long l, r;
			if (P.first % 2 == 0) {
				l = P.first / 2 - 1;
				r = P.first / 2;
			} else {
				l = r = P.first / 2;
			}
			K -= P.second;
			if (K <= 0) {
				printf("Case #%d: %lld %lld\n", tc, r, l);
				break;
			}
			M[l] += P.second;
			M[r] += P.second;
		}
	}
}
