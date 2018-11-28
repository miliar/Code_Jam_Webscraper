#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 105;

int n, p;
int g[MAX_N];

void input() {
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++) {
		scanf("%d", &g[i]);
	}
}

int work() {
	int remainder[10] = {0};
	for (int i = 0; i < n; i++) {
		remainder[g[i] % p]++;
	}
	if (p == 2) {
		return remainder[0] + (remainder[1] + 1) / 2;
	}
	if (p == 3) {
		int a = min(remainder[1], remainder[2]);
		int b = max(remainder[1], remainder[2]);
		int ret = remainder[0] + a + (b - a + 2) / 3;
		return ret;
	}
	int a = min(remainder[1], remainder[3]);
	int b = max(remainder[1], remainder[3]);
	int c = remainder[2];
	int ret = remainder[0] + a + c / 2;
	b -= a;
	c %= 2;
	if (c == 1 && b >= 2) {
		ret++;
		c -= 1;
		b -= 2;
	}
	ret += b / 4;
	b %= 4;
	if (c != 0 || b != 0) {
		ret++;
	}
	return ret;
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d: ", case_num);
		input();
		printf("%d\n", work());
	}
	return 0;
}
