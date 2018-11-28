#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	int j;
	for (j = 1 ; j <= tc ; j++) {
		char arr[108];
		scanf("%s", arr);
		int len = 0;
		while (arr[len] != '\0') {
			len++;
		}
		int k;
		int loop = 1;
		while (loop) {
			loop = 0;
			for (k = 0 ; k < len - 1 ; k++) {
				if (arr[k] > arr[k + 1]) {
					loop = 1;
					break; 
				}
			}
			if (loop == 1) {
				arr[k] -= 1;
				k += 1;
				for ( ; k < len ; k++) {
					arr[k] = '9';
				}
			}
		}
		if (arr[0] > '0') {
			printf("Case #%d: %s\n", j, arr);
		} else {
			printf("Case #%d: %s\n", j, arr + 1);
		}
	}
	return 0;
}
