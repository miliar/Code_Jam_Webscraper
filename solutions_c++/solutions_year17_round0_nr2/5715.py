#include <cstdio>
typedef unsigned long long ull;
int tc,tcn;
ull n, re;

ull get(ull n, ull num) {
	ull ret = 0;
	ull cur = 0;
	ull t = 1;
	ull st = 1;
	while( t*10<=n)
		t *= (ull)10;
	for (ull i = 0; i < num; i++,t/=10) {
		for (ull j = st; j <= 9; j++) {
			ull tmp = ret;
			bool pos = 1;
			for (ull k = 1; k <= t; k*=10) {
				tmp += k*j;
				if (tmp > n) {
					pos = 0;
					break;
				}
			}
			if (!pos) {
				ret += (j-1)*t;
				st--;
				break;
			}
			else if (j == 9) {
				ret += j*t;
			}
			else
				st++;
		}
		
	}

	return ret;
}

void solve() {
	scanf("%d", &tc);
	while (tc--) {
		int num = 0;
		scanf("%llu", &n);
		for (ull i = 1; i <= n; i *= 10)
			num++;
		re = 0;
		while (!re && num) {
			re = get(n, (ull)num);
			--num;
		}
		printf("Case #%d: %llu\n", ++tcn, re);
	}
}

int main(void) {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	solve();
	return 0;
}
