#include<bits/stdc++.h>
int main() {
	int T;
	scanf("%d", &T);
	for (int tT = 1 ; tT <= T ; tT++) {
		char tmp, S[1005];
		int n = 0, flipper, start = -1, impossible = 0;
		while (scanf("%c", &tmp) && tmp != ' ') {
			//'+' = 1, '-' = 0
			if (tmp == '+') {
				S[n] = 1;
			}
			else if (tmp == '-') {
				S[n] = 0;
				if (start == -1) {
					start = n;
				}
			}
			n++;
		}
		S[n] = -1;
		scanf("%d", &flipper);
		int counterZero = 0, flipTime = 0;
		if (start == -1) {
			start = n;
		}
		for (int i = start ; i < n ; i++) {
			// printf("i = %d: ", i);
			// for (int s = start; s < n; s++) {
			// 	printf("%d", S[s]);
			// }
			// printf("\n");
			counterZero = 0;
			if (S[i] == 0) {
				if (i + flipper > n) {
					impossible = 1;
					break;
				}
				for (int k = 0 ; k < flipper ; k++) {
					if (S[i + k] == 0) {
						S[i + k] = 1;
					}
					else {
						S[i + k] = 0;
						counterZero++;
					}
				}
				flipTime++;
			}
			
		}
		printf("Case #%d: ", tT);

		if (impossible || counterZero) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%d\n", flipTime);
		}
	}
	return 0;
}