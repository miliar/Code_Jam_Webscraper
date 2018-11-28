#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <omp.h>
using namespace std;

int main() {
	int Tn;
	scanf("%d", &Tn);

	for (int Tc = 1; Tc <= Tn; ++Tc) {
		char s[10000];
		int K;
		scanf("%s%d", s, &K);

		int ans = 0;

		int l = strlen(s);
		for (int i = 0; i <= l - K; ++i) {
			if (s[i] == '-') {
				++ans;
				for (int j = 0; j < K; ++j)
					s[i + j] = (s[i + j] == '+' ? '-' : '+');
			}
		}


		for (int i = l - K + 1; i < l; ++i)
			if (s[i] == '-') ans = -1;



		printf("Case #%d: ", Tc);

		if (ans == -1) {
			printf("IMPOSSIBLE\n");
		}else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
