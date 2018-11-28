#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solvation(FILE* f1, FILE* f2, int inum) {
	int i = 0, k, s, ans = 0;
	char c;
	char arr[1010];
	fscanf_s(f1, "%c", &c);
	while (i < 10000) {
		fscanf_s(f1, "%c", arr+i);
		if (arr[i] == ' ') {
			break;
		}
		i++;
	}
	s = i;
	fscanf_s(f1, "%d", &k);
	i = 0;
	while (i < s) {
		if (arr[i] == '+') {
			i++;
			continue;
		}
		if (i > s - k) {
			fprintf_s(f2, " IMPOSSIBLE");
			return 0;
		}
		ans++;
		int ind = i;
		for (int j = 0; j < k; j++) {
			if (arr[ind] == '+') {
				arr[ind] = '-';
			}
			else {
				arr[ind] = '+';
			}
			ind++;
		}
		i++;
	}
	fprintf_s(f2, " %d", ans);
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
		fprintf_s(f2, "Case #%d:", inum + 1);
		ans = solvation(f1, f2, inum);
		fprintf_s(f2, "\n");
	}
	fclose(f1);
	fclose(f2);
	return 0;
}