#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;


int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		char S[1001];
		int K;
		scanf("%s %d", S, &K);
		size_t len = strlen(S);

		int flip = 0;
		for (size_t i = 0; i <= len - K; ++i) {
			if (S[i] == '+') {
				continue;
			}
			
			for (int j = 0; j < K; ++j) {
				S[i + j] = S[i + j] == '+' ? '-' : '+';
			}
			++flip;
		}

		if (find(S, S + len, '-') == S + len) {
			printf("Case #%d: %d\n", Ti, flip);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", Ti);
		}
	}
	return 0;
}
