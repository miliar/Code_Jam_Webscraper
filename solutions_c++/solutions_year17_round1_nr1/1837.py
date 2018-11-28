#include <stdio.h>

char cake[25][26];

void fill(int sx, int sy) {
	char c = cake[sy][sx];
	for (int x = sx; x >= 0; x--) {
		if (cake[sy][x] == '?' || cake[sy][x] == c) {
			cake[sy][x] = c;
		}
		else {
			break;
		}
	}
}

void fillRight(int sx, int sy, int w, char c) {
	int x;
	for (x = sx; x < w; x++) {
		if (cake[sy][x] != '?') throw "";
		cake[sy][x] = c;
	}
}

void solve() {
	int h, w;
	scanf("%d %d", &h, &w);
	for (int i = 0; i < h; i++) {
		scanf("%s", cake[i]);
	}

	for (int y = 0; y < h; y++) {
		char lastC = 0;
		int lastX = -1;
		for (int x = 0; x < w; x++) {
			if (cake[y][x] != '?') {
				lastC = cake[y][x];
				lastX = x;
				fill(x, y);
			}
		}
		if (lastC) {
			fillRight(lastX + 1, y, w, lastC);
		}
	}

	for (int y = 0; y < h - 1; y++) {
		for (int x = 0; x < w; x++) {
			if (cake[y + 1][x] == '?') {
				cake[y + 1][x] = cake[y][x];
			}
		}
	}
	for (int y = h - 1; y >= 1; y--) {
		for (int x = 0; x < w; x++) {
			if (cake[y - 1][x] == '?') {
				cake[y - 1][x] = cake[y][x];
			}
		}
	}

	printf("\n");
	for (int i = 0; i < h; i++) {
		printf("%s\n", cake[i]);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
