#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

long long ans;
int n;
char ch[20];
int a[20];

void solve(int x) {
	for (int i = 1; i < x; ++i) {
		if (a[i] < a[i-1]) {
			a[i-1] -= 1;
			for (int j = i; j < x; ++j) {
				a[j] = 9;
			}
			solve(i);
			return;
		}
	}
}


void work() {
	scanf("%s", ch);
	n = strlen(ch);
	for (int i = 0; i < n; ++i) {
		a[i] = ch[i] - '0';
	}
	solve(n);
	ans = 0;
	for (int i = 0; i < n; ++i) {
		ans *= 10;
		ans += a[i];
	}
	printf("%lld\n", ans);
}

int main() {
	int TC;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		printf("Case #%d: ", tc);
		work();
	}
	
}