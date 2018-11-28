#include <stdio.h>

long long int a, b;
void go(long long int n, long long int k) {
	if (k == 1) {
		a = n /2;
		b = (n -1) /2;
	} else {
		long long int l_empty = (n -1) /2;
		long long int r_empty = n /2;
		long long int k_small = (k -1)/2;
		long long int k_large = k/2;
		if (k % 2 == 0) 
			go(r_empty, k_large);
		else
			go(l_empty, k_small);
	}
}
int main()
{	int T;
	long long int n, k;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%lld %lld", &n, &k);
		go(n, k);
		printf("Case #%d: %lld %lld\n", t, a, b);
	}
	return 0;
}
