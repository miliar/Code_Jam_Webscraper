#include <bits/stdc++.h>
#define intl long long
using namespace std;

intl n, ans, base;
int t_, T;

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		scanf("%lld",&n);
		ans = 0;
		for (int t = 18; t >= 0; t--) {
			intl base = 1;
			for (int i = 1; i <= t; i++) base = base * 10LL + 1LL;
			while (ans + base <= n && ans % 10LL != 9LL) ans += base;
		}
		printf("Case #%d: %lld\n",++t_, ans);
	}
	return 0;
}
