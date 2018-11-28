#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define Pi1 3.1415926535
#define Pi2 0.000000000089793238462643

int ra[1001];
int h[1001];
double s[1001];
double s2[1001];

void quickSort1(int l, int r) {
	double x = s[(l + r) / 2];

	int i = l;
	int j = r;
	while (i <= j)
	{
		while (s[i] < x) i++;
		while (s[j] > x) j--;
		if (i <= j)
		{
			double xx = s[i];
			s[i] = s[j];
			s[j] = xx;
			xx = s2[i];
			s2[i] = s2[j];
			s2[j] = xx;
			int y = ra[i];
			ra[i] = ra[j];
			ra[j] = y;
			y = h[i];
			h[i] = h[j];
			h[j] = y;
			i++;
			j--;
		}
	}
	if (i<r)
		quickSort1(i, r);

	if (l<j)
		quickSort1(l, j);
}

int solvation(FILE* f1, FILE* f2, int inum) {
	int i = 0, j, n, k, ans = 0;
	double max = 0;
	double max2 = 0;
	fscanf_s(f1, "%d %d", &n, &k);
	for (i = 0; i < n; i++) {
		fscanf_s(f1, "%d %d", ra+i, h+i);
		s[i] = 2 * double(ra[i])*double(h[i])*Pi1;
		s2[i] = 2 * double(ra[i])*double(h[i])*Pi2;
	}
	quickSort1(0, n - 1);
	for (i = 0; i <n; i++) {
		int rad = ra[i];
		int he = h[i];
		double res = double(rad)*double(rad)*Pi1;
		double res2 = double(rad)*double(rad)*Pi2;
		res += s[i];
		res2 += s2[i];
		int num = 1;
		for (j = n-1; j >=0; j--) {
			if (i == j) {
				continue;
			}
			if (num >= k) {
				break;
			}
			if (ra[j] <= rad) {
				res += s[j];
				res2 += s2[j];
				num++;
			}
		}
		if (num == k && res > max) {
			max = res;
			max2 = res2;
		}
		if (res < 10) {
			res = res;
		}
	}
	long long t = long long(max);
	long long t2 = long long(max2);
	long long tt = t + t2;
	double x = max - t;
	double x2 = max2 - t2;
	double xx = x + x2;
	if (xx > 1) {
		xx = xx - 1;
		tt++;
	}
	long long st = 1000000000;
	long long ttt = long long(xx * 1000000000);
	fprintf_s(f2, "%lld", tt);
	fprintf_s(f2, ".");
	st /= 10;
	while (ttt < st && st > 0) {
		fprintf_s(f2, "0");
		st /= 10;
	}
	fprintf_s(f2, "%lld\n", ttt);
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
		fprintf_s(f2, "Case #%d: ", inum + 1);
		ans = solvation(f1, f2, inum);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}