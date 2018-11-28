#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#define arr_size 30
using namespace std;

char solve_outermostDigit(char arr[arr_size], int offset) {
	char outermostDigit = arr[offset];
	for (int i = offset; i < arr_size; i++) {
		if (arr[i] == 0) {
			break;
		}
		if (arr[i] < outermostDigit) {
			return outermostDigit - 1;
		}
		if (arr[i] > outermostDigit) {
			return outermostDigit;
		}
	}
	return outermostDigit;
}

int main() {
	//freopen("in.txt", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		char arr[arr_size] = { 0 };
		bool flag = false;
		scanf("%s\n", &arr);

		printf("Case #%d: ", i);
		for (int i = 0; i < arr_size; i++) {
			if (arr[i] == 0) {
				break;
			}
			if (flag) {
				printf("9");
			}
			else {
				char ans = solve_outermostDigit(arr, i);
				if (ans != arr[i]) {
					flag = true;
				}
				if (ans != '0') {
					printf("%c", ans);
				}
			}
		}
		printf("\n");
	}

	return 0;
}