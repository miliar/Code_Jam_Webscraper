#include <iostream>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.large.out", "w", stdout);
	char dummy;
	// your code goes here
	int tc = 0;
	scanf("%d", &tc);
	scanf("%c", &dummy);
	for (int q = 1; q <= tc; q++) {
		char c[1005];
		int len = 0;
		int flip = 0;
		char temp;
		while (scanf("%c", &temp)) {
			if (temp == ' ') {
				break;
			}
			c[len] = temp;
			len++;
		}
		scanf("%d", &flip);
		scanf("%c", &dummy);
		int count = 0;
		for (int i = 0; i <= len - flip; i++) {
			if (c[i] == '+') continue;
			count++;
			for (int j = i; j < i + flip; j++) {
				if (c[j] == '-') {
					c[j] = '+';
				}
				else {
					c[j] = '-';
				}
			}
		}
		bool flag = false;
		for (int i = len-flip+ 1; i < len; i++) {
			if (c[i] == '-') {
				flag = true;
				break;
			}
		}
		if (flag) {
			printf("Case #%d: IMPOSSIBLE\n", q);
		}
		else {
			printf("Case #%d: %d\n", q, count);
		}
	}
	
	return 0;
}
