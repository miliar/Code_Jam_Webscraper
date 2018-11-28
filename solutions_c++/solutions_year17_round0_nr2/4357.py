#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

int main() {

	int t;
	scanf("%d", &t);

	for (int testCase = 1; testCase <= t; testCase++) {

		char c[30];
		scanf("%s", c);

		int len = strlen(c);
		int i;
		for (i = 1; i < len; i++) {
			if (c[i - 1] > c[i]) {
				c[i - 1]--;
				for (int j = i; j < len; j++) {
					c[j] = '9';
				}
				break;
			}
		}

		for (int k = i-1; k > 0; k--) {
			if (c[k] < c[k - 1]) {
				c[k] = '9';
				c[k - 1]--;
			}
		}

		if (c[0] == '0') {
			for (int i = 0; i < len; i++) {
				c[i] = c[i + 1];
			}
		}

		printf("Case #%d: %s\n", testCase, c);
	}


	return 0;
}