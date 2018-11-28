#include <stdio.h>
#include <string.h>
#include <algorithm>
#define INF (1000000009)
#define MAXN (1005)
using namespace std;

char str[MAXN];
int T, N, K, Ans;

int main() {
	scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
		scanf(" %s %d", str, &K);
		N = (int)strlen(str); Ans = 0;
		for(int i = 0; i+K <= N; i++)
			if('-' == str[i]) {
				for(int j = i; j < i+K; j++)
					str[j] = ('+' == str[j]) ? '-' : '+';
				Ans++;
			}
		for(int i = 0; i < N; i++) if('-' == str[i]) Ans = INF;
		printf("Case #%d: ", t_i);
		printf(INF == Ans ? "IMPOSSIBLE\n" : "%d\n", Ans);
	}
	return 0;
}
