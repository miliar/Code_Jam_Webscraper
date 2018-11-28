#include <stdio.h>
#include <algorithm>
#include <string.h>

int num[30];
int min[30];

void solve() {
	long long int n; scanf("%lld", &n);

	int len = 0;
	for (; n > 0; n /= 10) {
		num[len] = n % 10;
		min[len] = num[len];
		len++;
	}
	for (int i = len; i < 25; i++) {
		num[len] = min[len] = 0;
	}
	if (len == 1) {
		printf("%d\n", num[0]);
		return;
	}

	for (int i = len - 2; i >= 0; i--) {
		if (num[i + 1] > num[i]) {
			for (int j = i + 1; j < len; j++) {
				if (num[j] != num[j + 1]) {
					num[j]--;

					int flag = 0;
					int top = 1;
					for (int k = len - 1; k >= 0; k--) {
						if (flag) {
							printf("9");
						}
						else {
							if (!top || num[k] != 0) {
								printf("%d", num[k]);
							}
							if (num[k] < min[k]) {
								flag = 1;
							}
						}
					}
					printf("\n");
					return;
				}
			}
		}
	}

	for (int i = len - 1; i >= 0; i--) {
		printf("%d", num[i]);
	}
	printf("\n");
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}