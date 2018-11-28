#include <stdio.h>
#include <string.h>
#include <memory.h>
#include <algorithm>

int gred[100];

int pack[100][100];

void solve() {
	int N, P; scanf("%d%d", &N, &P);

	for (int i = 0; i < N; i++) {
		scanf("%d", gred + i);
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < P; j++) {
			scanf("%d", &pack[i][j]);
		}
		std::sort(pack[i], pack[i] + P);
	}

	int cnt = 0;
	int pos[100];
	memset(pos, 0, sizeof(pos));

	for (int i = 0; i < P; i++) {
		int mingred = (pack[0][i] * 10 - 1) / 11 + 1;
		int maxgred = (pack[0][i] * 10) / 9;

		int min = -1, max = -1;
		
		for (int j = mingred / gred[0] - 3; (j - 3) * gred[0] <= maxgred; j++) {
			if (min < 0 && j * gred[0] <= maxgred && j * gred[0] >= mingred) min = j;
			if ((j + 1) * gred[0] > maxgred && j * gred[0] <= maxgred) max = j;
		}

		if (min < 0 || max < 0 || min > max) continue;
		int available = 1;

		for (int j = 1; j < N; j++) {
			while (pos[j] < P && (min * gred[j] * 9 - 1) / 10 + 1 > pack[j][pos[j]]) pos[j]++;
		}

		for (int j = 1; j < N; j++) {
			if (pos[j] >= P || (max * gred[j] * 11) / 10 < pack[j][pos[j]]) {
				available = 0; 
				break;
			}
		}

		if (available) {
			for (int j = 1; j < N; j++) {
				pos[j]++;
			}
		}

		cnt += available;
	}

	printf("%d\n", cnt);
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}