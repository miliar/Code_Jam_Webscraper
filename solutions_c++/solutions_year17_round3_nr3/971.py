#include <cstdio>

using namespace std;
typedef long double Double;

int t, n, k;
Double u, p[51], size, left, mid, ans;

int check(Double t) {
	Double rest = u;
	for(int i = 0; i < n; ++i) {
		if(p[i] <= t) {
			rest -= (t - p[i]);
			if(rest < 0) return 0;
		}
	}
	return rest >= 0;
}

int main() {
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		scanf("%d%d%Lf", &n, &k, &u);
		for(int i = 0; i < n; ++i) {
			scanf("%Lf", p+i);
		}
		
		left = 0.0L;
		size = 1.0L;
		while(size) {
			mid = left + size / 2.0L;
			if(check(mid)) {
				ans = left = mid;
			}
			size /= 2.0L;
		}
		
		size = ans;
		ans = 1.0;
		for(int i = 0; i < n; ++i) {
			if(p[i] <= size) {
				ans *= size;
			} else {
				ans *= p[i];
			}
		}
		
		printf("Case #%d: %Lf\n", tc, ans);
	}
	return 0;
}
