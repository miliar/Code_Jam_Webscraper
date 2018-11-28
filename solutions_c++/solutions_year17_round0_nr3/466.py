#include <stdio.h>
#include <stdlib.h>

int t, T;
long long int n, k;
long long int a, ca, cb, cnt;

int main() {
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		scanf("%lld %lld", &n, &k);
		a = n;
		ca = 1;
		cb = 0;
		cnt = 0;
		long long int i = 1;
		while(cnt + i < k) {
			if(a % 2 == 1) {
				ca = ca + ca + cb;
			} else {
				cb = ca + cb + cb;
			}
			a = (a - 1) / 2;
			cnt += i;
			i *= 2;
		}
		if(k - cnt <= cb) {
			printf("Case #%d: %lld %lld\n", t, (a + 1) / 2, a / 2);
		} else {
			printf("Case #%d: %lld %lld\n", t, a / 2, (a - 1) / 2);
		}
	}
	return 0;
}
