#include <cstdio>
#include <cstring>

int main()
{
	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; ++i) {
		printf("Case #%d: ", i+1);

		char S[1024];
		scanf("%s", S);

		int nS = strlen(S);
		for(int j = 0; j < nS-1; ++j) {
			if(S[j] > S[j+1]) {
				int same = j;
				for(; same > 0; --same) {
					if(S[same] != S[same - 1])
						break;
				}
				if(same == 1 && S[1] == S[0])
					same = 0;
				// printf("%d\t", same);

				-- S[same];
				for(int k = same + 1; k < nS; ++k) {
					S[k] = '9';
				}
				break;
			}
		}

		// puts(S);
		for(int i = 0; i < nS; ++i) {
			if(S[i] != '0') {
				printf("%s\n", S + i);
				break;
			}
		}
	}

	return 0;
}
