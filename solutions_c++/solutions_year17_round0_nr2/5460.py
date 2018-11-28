#include <cstdio>
typedef long long ll;
int N[21], len;
int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		ll num; scanf("%lld", &num);
		for (len = 0; num; len++, num /= 10)
			N[len] = num % 10;
		for (int i = 0; i < len - 1; i++) {
			if (N[i] < N[i + 1]) {
				N[i + 1]--;
				for (int j = i; j >= 0; j--)
					N[j] = 9;
			}
		}
		ll sum = 0;
		for (int i = len - 1; i >= 0; i--) {
			sum *= 10;
			sum += N[i];
		}
		printf("Case #%d: %lld\n", t, sum);
	}
	return 0;
}