#include <cstdio>
bool check(int a) {
	int cur;
	cur = a % 10;
	a /= 10;
	while(a > 0) {
		if(a % 10 > cur)
			return false;
		cur = a % 10;
		a /= 10;
	}
	return true;
}
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t, n;
	scanf("%d", &t);
	for(int x=1;x<=t;++x) {
		scanf("%d", &n);
		for(int i=n;i>=1;--i) {
			if(check(i)) {
				printf("Case #%d: %d\n", x, i);
				break;
			}
		}
	}
	return 0;
}
