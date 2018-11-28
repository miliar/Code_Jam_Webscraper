#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;
void swch(int *a, int n, int max) {
	if (n == max + 1) {
		return;
	}
	if (*(a + n) >= *(a + n - 1)) {
		swch(a, n + 1, max);
	}
	else {
		for (int i = n; i <= max; i++) {
			*(a + i) = 9;
		}
		*(a + n - 1) += 9;
		*(a + n - 1) %= 10;
		swch(a, n - 1, max);
	}
}
int main() {
	FILE* fi;
	fi = fopen("input.txt", "r");
	FILE* fo;
	fo = fopen("output.txt", "w");

	char arr[24];
	int number[24];
	int T, len;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%s", arr);
		len = strlen(arr);
		number[0] = 0;
		for (int i = 1; i <= len; i++) {
			number[i] = arr[i - 1] - '0';
		}
		swch(number, 1, len);
		fprintf(fo, "Case #%d: ", t);
		if (number[1] != 0) {
			fprintf(fo, "%d", number[1]);
		}
		for (int i = 2; i <= len; i++) {
			fprintf(fo, "%d", number[i]);
		}
		fprintf(fo, "\n");
	}
	fclose(fo);
	fclose(fi);
	return 0;
}