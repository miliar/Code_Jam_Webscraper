#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a < b ? b : a)

struct interval {
	int a, b, r;
	bool used;
};

int n;
inline int next(int i) {
	if (i >= n - 1)
		return 0;
	else
		return i + 1;
}

bool ints_comp(interval i, interval j) {
	return i.a < j.a;
}

void execute_next(int test, FILE *f, FILE *gg) {
	int a1, a2;
	fscanf(f, "%d %d\n", &a1, &a2);
	n = a1 + a2;
	vector<interval> ints(n);
	for (int i = 0; i < a1; i++) {
		fscanf(f, "%d %d\n", &ints[i].a, &ints[i].b);
		ints[i].r = 0;
		ints[i].used = false;
	}
	for (int i = a1; i < a1 + a2; i++) {
		fscanf(f, "%d %d\n", &ints[i].a, &ints[i].b);
		ints[i].r = 1;
		ints[i].used = false;
	}
	sort(ints.begin(), ints.end(), ints_comp);
	int result = 0;
	int r_bad = -1, sum = 1440;
	if (a1 == 0) {
		r_bad = 1;
	} else if (a2 == 0) {
		r_bad = 0;
	} else {
		int start = 1;
		while (ints[start].r == ints[start - 1].r)
			start++;
		int sumr[2] = { 0, 0 };
		int i1 = start;
		do {
			int i2 = i1;
			while (ints[i1].r == ints[next(i2)].r)
				i2 = next(i2);
			int minutes = ints[i2].b - ints[i1].a;
			if (minutes < 0)
				minutes += 1440;
			sumr[ints[i2].r] += minutes;
			result++;
			i1 = next(i2);
		} while (i1 != start);
		for (int r = 0; r < 2; r++) {
			if (sumr[r] > 720) {
				sum = sumr[r];
				r_bad = r;
			}
		}
	}
	if (r_bad >= 0) {
		while (sum > 720) {
			int i_use, max = 0;
			for (int i = 0; i < n; i++) {
				int i2 = next(i);
				if (!ints[i].used && ints[i].r == r_bad && ints[i2].r == r_bad) {
					int minutes = ints[i2].a - ints[i].b;
					if (minutes < 0)
						minutes += 1440;
					if (minutes > max) {
						max = minutes;
						i_use = i;
					}
				}
			}
			sum -= max;
			ints[i_use].used = true;
			result += 2;
		}
	}
	
	fprintf(gg, "Case #%d: %d\n", test + 1, result);
}

int main(int argc, char* argv[])
{
	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;
	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		execute_next(test, f, g);
		printf("%d\n", test + 1);
	}
	fclose(f);
	fclose(g);
	return 0;
}

