#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 10;
char S[N];
char T[15] = "IMPOSSIBLE";
void xord(int ind) {
	if(S[ind] == '+') {
		S[ind] = '-';
	}
	else {
		S[ind] = '+';
	}
}

int solve(int K) {
	int n = strlen(S + 1);
	int ans = 0;
	for(int i = 1; i <= n; ++i) {
		int j = i + K - 1;
		if(j > n || S[i] == '+') {
			continue;
		}
		for(int k = i; k <= j; ++k) {
			xord(k);
		} 
		++ans;
	}
	int yes = 1;
	for(int i = 1; i <= n; ++i) 
		yes &= S[i] == '+';
	if(yes) {
		return ans;
	}
	return -1;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		int K;
		scanf("%s %d", S + 1, &K);
		int ans = solve(K);
		printf("Case #%d: ", tc);
		if(ans == -1) {
			printf("%s\n", T);
		}
		else {
			printf("%d\n", ans);
		}
	}
}