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

void execute_next(int test, FILE *f, FILE *g) {
	std::string row(1100, 0);
	fgets(&row[0], 1100, f);
	int k;
	for (int i = 0; i < row.size(); i++) {
		if (row[i] != '-' && row[i] != '+') {
			sscanf(&row[i+1], "%d", &k);
			row.resize(i);
			break;
		}
	}

	int flips = 0;
	for (int i = 0; i < row.size(); i++) {
		if (row[i] == '+')
			continue;
		if (i + k > row.size()) {
			flips = -1;
			break;
		}
		for (int j = i; j < i + k; j++)
			row[j] = row[j] == '+' ? '-' : '+';
		flips++;
	}

	printf("%d\n", test + 1);
	if (flips < 0) {
		fprintf(g, "Case #%d: %s\n", test + 1, "IMPOSSIBLE");
	} else {
		fprintf(g, "Case #%d: %d\n", test + 1, flips);
	}
}

int main(int argc, char* argv[])
{
	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;
	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		execute_next(test, f, g);
	}
	fclose(f);
	fclose(g);
	return 0;
}

