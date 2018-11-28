#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int rec(long long n, long long k, long long &min, long long &max) {
	if (k == 1) {
		min = (n - 1) / 2;
		max = n / 2;
		return 0;
	}
	if (n % 2 == 1) {
		rec(n / 2, k / 2, min, max);
	}
	else {
		if (k % 2 == 1) {
			rec((n - 1) / 2, k / 2, min, max);
		}
		else {
			rec(n / 2, k / 2, min, max);
		}
	}
	return 0;
}

int solvation(FILE* f1, FILE* f2, int inum) {
	long long n, k;
	long long min, max;
	fscanf_s(f1, "%lld %lld", &n, &k);
	rec(n, k, min, max);
	fprintf_s(f2, " %lld %lld", max, min);
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