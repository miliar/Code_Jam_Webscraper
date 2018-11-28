// Problem C. Bathroom Stalls
#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		long long n, k, m;
		scanf("%lld %lld", &n, &k);

		for (m = 1; k > m; m += m) {
			n -= m;
			k -= m;
		}
		long long t = n / m + (n % m >= k ? 1 : 0);
		printf("Case #%d: %lld %lld\n", ti, t / 2, (t - 1) / 2);
	}

	return 0;
}
