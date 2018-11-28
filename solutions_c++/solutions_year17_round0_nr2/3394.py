#include <stdio.h>
#define ll long long

int t, sz, a, b;
ll n, s;
int main() {
	freopen("c:\\input.txt", "r", stdin);
	freopen("c:\\output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%lld", &n);
		int chk = 1;
		int chk2 = 0;
		ll digit = 10;
		s = 0;
		while (chk) {
			chk = 0;
			digit = 10;
			s = 0;
			while (n / digit) {
				a = (n / digit) % 10;
				b = (n / (digit / 10)) % 10;
				if (a > b || b == 0) {
					n += (ll)(9 - b)*(digit / 10);
					s = digit;
					chk = 1;
				}
				digit *= 10;
			}
			if (chk2 == 0) {
				n -= s;
				chk2 = 1;
			}
		}
		printf("Case #%d %lld\n", tc, n);
	}
}