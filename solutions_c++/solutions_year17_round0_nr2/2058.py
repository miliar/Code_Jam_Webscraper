#include <cstdio>
#include <algorithm>

using namespace std;

unsigned long long a, n;

void dfs(unsigned long long c, int r) {
	a = max(a, c);
	for(int i = r;i <= 9;i++) {
		if(c * 10 + i > n) break;
		dfs(c * 10 + i, i);
	}
}

void sol() {
	scanf("%llu", &n);
	a = 0;
	dfs(0, 1);
	printf("%llu\n", a);
}

int main() {
	int t; scanf("%d", &t);
	for(int i = 1;i <= t;i++) printf("Case #%d: ", i), sol();
}
