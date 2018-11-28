#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[]) {
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		int K = 0, total = 1e9;
		char S[1001];
		S[1000] = '\0';
		scanf("%s %d", S, &K);
		int N = strlen(S);
		int total_left = 0, total_right = 0;
		for(int k = 0; k < 2; k++) {
			int sub_total = 0;
			char s[1001];
			s[1000] = '\0';
			for(int i = 0; i < N/2; i++) {
				char temp = S[i];
				S[i] = S[N - i - 1];
				S[N - i - 1] = temp;
			}
			for(int i = 0; i < N; i++)
				s[i] = S[i];
			for(int i = 0; i <= (N - K); i++) {
				if(s[i] == '-') {
					sub_total++;
					for(int j = 0; j < K; j++) {
						s[i + j] = (s[i + j] == '-')?'+':'-';
					}
				}
			}
			for(int i = 0; i < N; i++) {
				if(s[i] == '-') {
					sub_total = -1;
				}
			}
			if(sub_total >= 0)
				total = min(total, sub_total);
		}
		printf("Case #%d: ", (t + 1));
		if(total >= 0 && total < 1e5)
			printf("%d\n", total);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}