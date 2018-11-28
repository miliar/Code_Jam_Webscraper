#include <iostream>
#include <cstdio>
using namespace std;

char str[1010];

int main() {
	int t;
	scanf("%d", &t);
	int ca = 1;
	while (t--) {
		printf("Case #%d: ", ca++);
		int k;
		scanf("%s%d", str, &k);
		int len = strlen(str), flag = 1, num = 0;
		for (int i = 0; i < len; i++) {
			if (str[i] == '-' && i + k <= len) {
				for (int j = i; j < i + k; j++) {
					if (str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				num++;
			} else if (str[i] == '-') {
				flag = 0;
			}
		}
		if (flag) {
			printf("%d\n", num);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
}
