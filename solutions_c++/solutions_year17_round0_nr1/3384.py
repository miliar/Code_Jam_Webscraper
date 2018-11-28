#include <cstdio>
#include <cstring>

int main()
{
	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; ++i) {
		printf("Case #%d: ", i+1);

		char S[1024];
		int K;
		scanf("%s %d", S, &K);

		if(K == 0) {

			int ns = strlen(S);
			int good = 1;
			for(int j = 0; j < ns; ++j) {
				if(S[j] == '-') {
					good = 0;
					break;
				}
			}

			if(good) {
				puts("0");
			} else {
				puts("IMPOSSIBLE");
			}

			continue;
		}

		int turn = 0;
		int ns = strlen(S);
		for(int j = 0; j < ns-K+1; ++j) {
			if(S[j] == '-') {
				++turn;
				S[j] = '+';
				for(int k = j+1; k < j+K; ++k) {
					if(S[k] == '-') {
						S[k] = '+';
					} else {
						S[k] = '-';
					}
				}
			}
		}

		// printf("%s\n", S);

		int good = 1;
		for(int j = ns - K; j < ns; ++j) {
			if(S[j] == '-') {
				good = 0;
				break;
			}
		}

		if(good) {
			printf("%d\n", turn);
		} else {
			puts("IMPOSSIBLE");
		}
	}

	return 0;
}
