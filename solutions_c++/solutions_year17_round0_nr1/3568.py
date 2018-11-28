#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
using namespace std;

char inv(char ch) {
	return ch == '+' ? '-' : '+';
}

void solve(int tst) {
	char S[2000];
	int K;
	cin >> S >> K;
	int len = strlen(S);

	int ans = 0;
	for (int i = 0; i + K - 1 < len; ++i) {
		if (S[i] == '-') {
			for (int j = 0; j < K; ++j) {
				S[i + j] = inv(S[i + j]);
			}
			++ans;
		}
	}

	for (int i = 0; i < len; ++i) {
		if (S[i] == '-') {
			printf("Case #%d: IMPOSSIBLE\n", tst);
			return;
		}

	}
	printf("Case #%d: %d\n", tst, ans);	
}

int main() {
	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}