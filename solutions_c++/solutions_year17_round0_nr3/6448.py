#include <cstdio>

int main() {
	int T, a;
	long long N, K, halfK, v[2][2], cnt[2][2], rng, ans;

	scanf("%d", &T);
	for (int Case = 1; Case <= T; Case++) {
		scanf("%lld%lld", &N, &K);
		halfK = K >> 1;
		a = 0; rng = 1;
		v[0][0] = N; v[0][1] = 0;
		cnt[0][0] = 1; cnt[0][1] = 0;
		while (halfK >= rng) {
			v[!a][0] = v[a][0] >> 1; v[!a][1] = v[!a][0] - 1;
			if (v[a][0] & 1) {
				cnt[!a][0] = (cnt[a][0] << 1) + cnt[a][1]; cnt[!a][1] = cnt[a][1];
			} else {
				cnt[!a][0] = cnt[a][0]; cnt[!a][1] = cnt[a][0] + (cnt[a][1] << 1);
			}
			a = !a;
			rng <<= 1;
		}
		if (K - rng + 1 <= cnt[a][0]) {
			ans = v[a][0];
		} else {
			ans = v[a][1];
		}
		if (ans & 1) {
			printf("Case #%d: %lld %lld\n", Case, ans >> 1, ans >> 1);
		} else {
			printf("Case #%d: %lld %lld\n", Case, ans >> 1, (ans >> 1) - 1);
		}
	}
	return 0;
}
