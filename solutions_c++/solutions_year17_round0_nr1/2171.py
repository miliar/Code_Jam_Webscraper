#include <iostream>
#include <cstring>
using namespace std;

int main() {
	char S[1010];
	int T, K;

	scanf("%d", &T);
	for (int caseN = 1; caseN <= T; caseN++) {
		scanf("%s%d", &S, &K);
		int ans = 0;
		for (int i = 0; i <= strlen(S) - K; i++) {
			if (S[i] == '-') {
				ans++;
				for (int j = i + 1; j < i + K; j++) {
					if (S[j] == '+') S[j] = '-';
					else S[j] = '+';
				}
			}
		}
		for (int i = strlen(S) - K + 1; i < strlen(S); i++) {
			if (S[i] == '-') ans = -1;
		}
		printf("Case #%d: ", caseN);
		if (ans < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}