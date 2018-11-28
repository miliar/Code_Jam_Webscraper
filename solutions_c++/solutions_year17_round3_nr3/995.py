#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double p[51];
double pp[51];

void quickSort1(int l, int r) {
	double x = p[(l + r) / 2];

	int i = l;
	int j = r;
	while (i <= j)
	{
		while (p[i] < x) i++;
		while (p[j] > x) j--;
		if (i <= j)
		{
			double xx = p[i];
			p[i] = p[j];
			p[j] = xx;
			i++;
			j--;
		}
	}
	if (i<r)
		quickSort1(i, r);

	if (l<j)
		quickSort1(l, j);
}


double solvation(FILE* f1, FILE* f2, int inum) {
	int i, n, k;
	double u;
	double s = 0;
	fscanf_s(f1, "%d %d", &n, &k);
	fscanf_s(f1, "%lf", &u);
	for (i = 0; i < n; i++) {
		fscanf_s(f1, "%lf", p+i);
		s += p[i];
	}
	if (s + u >= n) {
		return 1;
	}
	double ss = s;
	quickSort1(0, n - 1);
	for (i = 0; i < n; i++) {
		pp[i] = p[i];
	}
	for (i = n - 1; i >= 0; i--) {
		double t = (ss + u) / (i + 1);
		if (t > 1) {
			t = 1;
		}
		if ( t >= p[i]) {
			for (int j = 0; j <= i; j++) {
				pp[j] = t;
			}
			double ans = 1;
			for (int j = 0; j < n; j++) {
				ans *= pp[j];
			}
			return ans;
		}
		ss -= p[i];
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	double ans = 0;
	FILE* f1;
	FILE* f2;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	for (int inum = 0; inum < tnum; inum++) {
		fprintf_s(f2, "Case #%d: ", inum + 1);
		ans = solvation(f1, f2, inum);
		fprintf_s(f2, "%lf\n", ans);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}