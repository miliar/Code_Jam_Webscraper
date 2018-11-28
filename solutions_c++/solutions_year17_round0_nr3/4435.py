#include <cstdio>

struct P {
	long long x, y;
};

P f(long long n, long long k) {
	if (n > 0 && k > 1) {
		long long x = (n - 1) / 2;
		long long y = (k - 1) / 2;

		P tmp1 = f(n - 1 - x, k - 1 - y);
		P tmp2 = f(x, y);
		
//		printf("(%lld %lld) -> (%lld %lld) (%lld %lld)\n", n, k, n - 1 - x, k - 1 - y, x, y);
		if (tmp1.x == -1) return tmp2;
		if (tmp2.x == -1) return tmp1;
		if (tmp1.x < tmp2.x) return tmp1;
		if (tmp1.x > tmp2.x) return tmp2;
		if (tmp1.y < tmp2.y) return tmp1;
		return tmp2;
	}

	P tmp;

	if (k == 1) {
		tmp.x = (n - 1) / 2;
		tmp.y = n - 1 - ((n - 1) / 2);

		return tmp;
	}

	tmp.x = -1;
	tmp.y = -1;

	return tmp;
}
int t;
long long n, k;
int main(){
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%lld %lld", &n, &k);

		P ans = f(n, k);
		printf("Case #%d: %lld %lld\n", i + 1, ans.y, ans.x);
	}
}
