#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int T;
char str[1001];
int K;
int main() {
	scanf("%d\n", &T);
	for (int TT = 1; TT <= T; TT++) {
		scanf("%s%d", str, &K);
		int i, ans = 0;
		for (i = 0; str[i + K - 1]; i ++) {
			if (str[i] == '-') {
				for (int j = 0; j < K; j++)
					str[i + j] = str[i + j] == '-' ? '+' : '-';
				ans ++;
			}
		}
		for (; str[i]; i++)
			if (str[i] != '+')
				ans = -1;
		printf("Case #%d: ", TT);
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}