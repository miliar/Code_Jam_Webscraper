#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < n; i ++)
typedef long long LL;
const int N = 20;

char answer[N], num[N];
int length;
LL memory[N][10][2];
LL base[N];

using namespace std;

LL dfs(bool limit, int prev_num, int K) {
	if (K == length) {
		return 0;
	}

	LL &res = memory[K][prev_num][limit];
	if (res != -2) {
		return res;
	}
	int top = limit ? int(num[K] - '0'): 9;

	for (int i = top; i >= prev_num; i --) {
		res = dfs(i == top && limit, i, K + 1);
		if (res != -1) {
			res = i*base[length - K - 1] + res;
			return res;
		}
	}

	res = -1;
	return -1;
}

int main() {
	int T;
	scanf("%d", &T);
	base[0] = 1;
	for (int i = 1; i <= 18; i ++) {
		base[i] = base[i - 1] * 10;
	}
	rep(cas, T) {
		scanf("%s", num);
		length = strlen(num);
		rep(i, N)
			rep(j, 10)
			rep(s, 2) {
				memory[i][j][s] = -2;
			}
		printf("Case #%d: %lld\n", cas + 1, dfs(true, 0, 0));
	}
	return 0;
}
