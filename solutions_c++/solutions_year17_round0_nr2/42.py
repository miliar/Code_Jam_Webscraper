#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
ll ones[20], zeroes[20];
int main() {
	zeroes[0] = ones[0] = 1;
	for (int i = 1; i <= 17; ++i) {
		zeroes[i] = zeroes[i - 1] * 10;
		ones[i] = ones[i - 1] * 10 + 1;
	}
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		ll ans = 0, N;
		scanf("%lld", &N);
		for (int i = 17; i >= 0; --i) {
			for (int d = 9; d >= 0; --d) {
				// ddddddd...d
				if (ans + d * ones[i] <= N) {
					ans += d * zeroes[i];
					break;
				}
			}
		}
		printf("Case #%d: %lld\n", cn, ans);
	}
}

