#include<cstdio>
#include<algorithm>
#include<string>

int n, a, x;
char s[20];

bool ok(int x) {
	sprintf(s, "%d", x);
	std::string y = s;
	std::string z = s;
	std::sort(y.begin(), y.end());
	return y == z;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &n);
	while (n --> 0) {
		scanf("%d", &x);
		while (!ok(x)) x--;
		printf("Case #%d: %d\n", ++a, x);
	}
}
