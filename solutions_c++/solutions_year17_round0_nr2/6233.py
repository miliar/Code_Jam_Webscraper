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
	char buffer[100];
	fgets(buffer, 100, f);
	int n = 0;
	while (buffer[n] >= '0' && buffer[n] <= '9')
		n++;
	buffer[n] = '\0';

	int i = 1;
	while (i < n) {
		if (buffer[i - 1] > buffer[i]) {
			buffer[i - 1]--;
			while (i < n) {
				buffer[i] = '9';
				i++;
			}
			i = 1;
		} else
			i++;
	}

	i = 0;
	while (buffer[i] == '0')
		i++;

	fprintf(g, "Case #%d: %s\n", test + 1, buffer + i);
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

