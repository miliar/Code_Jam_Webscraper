#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;
int tt;
char input[1005];
char flip(char c) {
	if (c == '-') return '+';
	return '-';
}
void solve() {
	int K;
	scanf("%s %d", input, &K);
	int N = strlen(input);
	int ans = 0; bool isImpossible = false;
	for(int i = N - 1; i >= K; i--) {
		if(input[i] == '+') continue;
		for(int j = 0; j < K; j++) {
			input[i - j] = flip(input[i - j]);
		}
		ans = ans + 1;
	}
	for (int i = 1; i < K; i++) {
		if (input[i] != input[i - 1]) isImpossible = true;
	}

	printf("Case #%d: ", tt);
	if (isImpossible) {
		printf("IMPOSSIBLE\n");
	} else {
		if (input[0] == '-') ans++;
		printf("%d\n", ans);
	}
}
int main() {
	int t; scanf("%d", &t);
	for(tt=1; tt <= t; tt++) solve();
}
