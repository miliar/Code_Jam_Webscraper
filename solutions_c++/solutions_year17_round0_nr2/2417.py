#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solvation(FILE* f1, FILE* f2, int inum) {
	int i = 0, s;
	char arr[1010];
	while (i < 100) {
		fscanf_s(f1, "%c", arr + i);
		if (arr[i] == '\n') {
			break;
		}
		i++;
	}
	s = i;
	for (i = s - 1; i > 0; i--) {
		if (arr[i] >= arr[i - 1]) {
			continue;
		}
		arr[i - 1]--;
		int j = i;
		while (j < s) {
			arr[j] = 57;
			j++;
		}
	}
	fprintf_s(f2, " ");
	int print = 0;
	for (i = 0; i < s; i++) {
		if (arr[i] > 48) {
			print = 1;
		}
		if (print) {
			fprintf_s(f2, "%c", arr[i]);
		}
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	int ans = 0;
	char c;
	FILE* f1;
	FILE* f2;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	fscanf_s(f1, "%c", &c);
	for (int inum = 0; inum < tnum; inum++) {
		fprintf_s(f2, "Case #%d:", inum + 1);
		ans = solvation(f1, f2, inum);
		fprintf_s(f2, "\n");
	}
	fclose(f1);
	fclose(f2);
	return 0;
}