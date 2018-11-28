#include <cstdio>

const int N = 30;

long long a, b;
int n;

int main() {
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%lld", &a);
		b = a;
		for (long long i = 10; i <= b; i *= 10) {
			if ((a / i % 10) > (a / (i / 10) % 10)) {
				a = b / i * i - 1;
			}
		}
		printf("Case #%d: %lld\n", cas, a);
	}
	return 0;
}
