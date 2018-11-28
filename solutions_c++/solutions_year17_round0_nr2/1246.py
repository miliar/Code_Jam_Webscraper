#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int T;
	char N[20];
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%s", &N);
		int len = strlen(N);
		for (int j = 0; j < len - 1; j++) {
			if (N[j] > N[j + 1]) {
				N[j] -= 1;
				for (int k = j + 1; k < len; k++) {
					N[k] = '9';                    
				}
				for (int k = j; k > 0; k--) {
					if (N[k] < N[k - 1]) {
						N[k] = '9';
						N[k - 1] -= 1;
					} else {
						break;
					}
				}
				break;
			}
		}
		printf("Case #%d: %s\n", i + 1, N[0] == '0' ? (N + 1) : N);
	}
	return 0;
}

