#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solvation(FILE* f1, FILE* f2, int inum) {
	int i = 0, j, n, k, s, ans = 0;
	int mini = -1, minj = -1;
	char c;
	char arr[30][30];
	fscanf_s(f1, "%d %d", &n, &k);
	fscanf_s(f1, "%c", &c);
	for (i = 0; i < n; i++) {
		for (j = 0; j < k; j++) {
			fscanf_s(f1, "%c", &arr[i][j]);
			if (arr[i][j] != '?' && mini < 0) {
				mini = i;
				minj = j;
			}
		}
		fscanf_s(f1, "%c", &c);
	}
	for (i = 0; i < mini; i++) {
		for (j = 0; j < k; j++) {
			arr[i][j] = arr[mini][j];
		}
	}
	for (i = 0; i < n; i++) {
		int hl = 0;
		int ha = 0;
		for (j = 0; j < k; j++) {
			if (arr[i][j] != '?') {
				hl = 1;
			}
			else {
				ha = 1;
			}
		}
		if (ha == 0) {
			continue;
		}
		if (hl == 0) {
			for (j = 0; j < k; j++) {
				arr[i][j] = arr[i - 1][j];
			}
			continue;
		}
		for (j = 0; j < k; j++) {
			if (arr[i][j] != '?') {
				s = j - 1;
				while (s >=0 && arr[i][s] == '?') {
					arr[i][s] = arr[i][j];
					s--;
				}
				s = j + 1;
				while (s < k && arr[i][s] == '?') {
					arr[i][s] = arr[i][j];
					s++;
				}
			}
		}

	}
	for (i = 0; i < n; i++) {
		for (j = 0; j < k; j++) {
			fprintf_s(f2, "%c", arr[i][j]);
		}
		fprintf_s(f2, "\n");
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	int ans = 0;
	FILE* f1;
	FILE* f2;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	for (int inum = 0; inum < tnum; inum++) {
		fprintf_s(f2, "Case #%d:\n", inum + 1);
		ans = solvation(f1, f2, inum);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}