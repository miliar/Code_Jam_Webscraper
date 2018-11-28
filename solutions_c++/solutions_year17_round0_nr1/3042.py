#include <bits/stdc++.h>

using namespace std;
const int MAXN = 1010;

int N, K;
char S[MAXN];
bool A[MAXN];

int go() {
	scanf("%s %d", S, &K);
	N = strlen(S);
	for (int i = 0; i < N; i++) {
		A[i] = (S[i] == '+');
	}

	int ans = 0;
	for (int i = 0; i < N; i++) {
		if (!A[i]) {
			ans++;
			//flip this one
			if (i + K > N) {
				return -1;
			}

			for (int j = i; j < i + K; j++) {
				A[j] ^= 1;
			}
		}
	}

	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	int nq;
	scanf("%d", &nq);
	freopen("output.txt", "w", stdout);
	for (int i = 1; i <= nq; i++) {
		printf("Case #%d: ", i);
		int ans = go();
		if (ans == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ans);
		}
	}
}
