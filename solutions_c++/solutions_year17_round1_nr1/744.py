#include <stdio.h>
#include <string.h>
#include <memory.h>

void solve() {
	int R, C; scanf("%d%d", &R, &C);
	char cell[30][30];
	int un[30];
	int last = 0;
	
	memset(un, 0, sizeof(un));


	for (int i = 0; i < R; i++) {
		scanf("%s", cell[i]);
		for (int j = 0; j < C; j++) {
			if (cell[i][j] == '?') un[i]++;
		}
		if (un[i] < C) last = i;
	}

	for (int i = 0; i <= last; i++) {
		if (un[i] == C) continue;
		char first = 0;
		for (int j = 0; j < C; j++) {
			if (cell[i][j] != '?') {
				first = cell[i][j];
				break;
			}
		}
		int idx = 0;
		while (idx < C && (cell[i][idx] == '?' || cell[i][idx] == first)) {
			cell[i][idx] = first;
			idx++;
		}
		char cur = 0;
		while (idx < C) {
			if (cell[i][idx] != '?') cur = cell[i][idx];
			else cell[i][idx] = cur;
			idx++;
		}
	}

	int idx = 0;
	int tar = 0;
	while (un[tar] == C) tar++;

	for (; idx < R && (un[idx] == C || idx == tar); idx++) {
		strcpy(cell[idx], cell[tar]);
	}
	for (; idx < R; idx++) {
		if (un[idx] < C) tar = idx;
		else strcpy(cell[idx], cell[tar]);
	}
	printf("\n");
	for (int i = 0; i < R; i++) {
		printf("%s\n", cell[i]);
	}
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