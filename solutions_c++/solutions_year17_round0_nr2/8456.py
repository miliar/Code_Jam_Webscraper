#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <list>
#include <set>
#include <map>

using namespace std;

int main(int argc, char *argv) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	getchar();
	for (int t = 0; t < T; t++) {
		int size;
		int N[19];
		for (int i = 0; i < 19; i++) {
			char n;
			scanf("%c", &n);
			if ('0' <= n && n <= '9') {
				N[i] = n - '0';
			}
			else {
				size = i;
				break;
			}
		}

		int is_changed = 20;
		for (int i = 0; i < size - 1; i++) {
			if (N[i] > N[i + 1]) {
				N[i] -= 1;
				is_changed = i;
				break;
			}
		}
		for (int i = is_changed; i > 0; i--) {
			if (N[i] < N[i - 1]) {
				N[i - 1] -= 1;
				is_changed = i - 1;
			}
			else {
				break;
			}
		}

		printf("Case #%d: ", t + 1);
		for (int i = 0; i < size; i++) {
			if (i == 0 && N[i] == 0) {

			}
			else if (i > is_changed) {
				printf("9");
			}
			else {
				printf("%d", N[i]);
			}
		}
		printf("\n");
	}
}