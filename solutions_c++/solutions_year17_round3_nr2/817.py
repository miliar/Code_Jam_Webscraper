#include <bits/stdc++.h>

using namespace std;

int span(int start, int end) {
	if (end > start) {
		return end - start;
	} else {
		return end + 1440 - start;
	}
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int t = 0; t < tc; t++) {
		int n, m;
		int startN[2], endN[2], startM[2], endM[2];
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &startN[i], &endN[i]);
		}
		
		for (int i = 0; i < m; i++) {
			scanf("%d %d", &startM[i], &endM[i]);
		}
		
		if (n == 0) {
			if (m == 1) {
				printf("Case #%d: %d\n", t + 1, 2);
			} else {
				// m == 2
				if (span(startM[0], endM[1]) <= 720 || span(startM[1], endM[0]) <= 720) {
					printf("Case #%d: %d\n", t + 1, 2);
				} else {
					printf("Case #%d: %d\n", t + 1, 4);
				}
			}
		} else if (m == 0) {
			if (n == 1) {
				printf("Case #%d: %d\n", t + 1, 2);
			} else {
				// n == 2
				if (span(startN[0], endN[1]) <= 720 || span(startN[1], endN[0]) <= 720) {
					printf("Case #%d: %d\n", t + 1, 2);
				} else {
					printf("Case #%d: %d\n", t + 1, 4);
				}
			}
		} else {
			printf("Case #%d: %d\n", t + 1, 2);
		}
	}
}
