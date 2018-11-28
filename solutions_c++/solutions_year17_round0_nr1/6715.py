#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	int k;
	for (k = 1 ; k <= tc ; k++) {
		char arr[1008];
		int j;
		scanf("%s %d", arr, &j);
		int counter = 0;
		int i = 0;
		while (arr[i + j - 1] != '\0') {
			if (arr[i] == '-') {
				counter++;
				int m;
				for (m = i ; m < i + j ; m++) {
					if (arr[m] == '-') {
						arr[m] = '+';
					} else {
						arr[m] = '-';
					}
				}
			}
			i++;
		}
		int s = 1;
		for (j = 0 ; arr[j] != '\0' ; j++) {
			if (arr[j] == '-') {
				s = 0;
				printf("Case #%d: IMPOSSIBLE\n", k);
				break;
			}
		}
		if (s == 1) {
			printf("Case #%d: %d\n", k, counter);
		}
	}
	return 0;
}
