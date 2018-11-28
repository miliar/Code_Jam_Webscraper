#include<bits/stdc++.h>

using namespace std;

const int MAXN = 1111;
char S[MAXN];
int f[MAXN][MAXN];
int K;

int work(){
	memset(f, 0x3f, sizeof(f));
	scanf("%s%d", S, &K);
	int l = strlen(S);
	int res = 0;
	for (int i = 0; i < l; ++i) {
		if (S[i] == '-') {
			++res;
			if (K + i > l) return -1;
			for (int k = 0; k < K; ++k) {
		//		if (k + i >= l) break;
				if (S[i+k] == '-') S[i+k] = '+';
				else S[i+k] = '-';
			}
		}
		//printf("%s %d\n", S, res);
	}
	return res;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int ans = work();
		printf("Case #%d: ", i);
		if (ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}

	return 0;
}
