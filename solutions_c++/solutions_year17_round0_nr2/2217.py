#include <stdio.h>
#include <string.h>
#include <deque>
#include <algorithm>
using namespace std;
#define MAX_N 20

char Number[MAX_N];

int main() {
	//freopen("input.in", "r", stdin);
	//freopen("output.out", "w", stdout);
	setbuf(stdout, NULL);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", Number);
		int N = strlen(Number);
		int beginModify = N;
		char prev = '9';
		int minus = 0;
		for (int i = N - 1; i >= 0; i--) {
			if (Number[i] == '0' && minus) {
				Number[i] = prev = '9';
				beginModify = i;
			}
			else{
				if (minus) {
					Number[i] -= 1;
					minus = 0;
				}
				if (Number[i] > prev) {
					if (Number[i] == '0') {
						Number[i] = '9';
						minus = 1;
						beginModify = i;
					}
					else {
						Number[i] -= 1;
						beginModify = i + 1;
					}
				}
				prev = Number[i];
			}
		}
		for (int i = beginModify; i < N; i++) Number[i] = '9';
		printf("Case #%d: %s\n", t, (Number[0] == '0' ? Number + 1 : Number));
	}
	return 0;
}