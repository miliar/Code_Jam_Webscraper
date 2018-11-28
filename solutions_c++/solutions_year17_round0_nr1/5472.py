#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;
void swch(char *a, int b) {
	for (int i = 0; i < b; i++) {
		if (*(a + i) == '-') {
			*(a + i) = '+';
		}
		else {
			*(a + i) = '-';
		}
	}
}
int main() {
	FILE* fi;
	fi = fopen("input.txt", "r");
	FILE* fo;
	fo = fopen("output.txt", "w");
	
	char arr[1004];
	int T;
	fscanf(fi,"%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%s", arr);
		int sum = 0, len, arrSize = strlen(arr), error = 0;
		fscanf(fi, "%d", &len);
		for (int i = 0; i < arrSize + 1 - len; i++) {
			if (arr[i] == '-') {
				swch(arr + i, len);
				sum++;
			}
		}
		for (int i = arrSize + 1 - len; i < arrSize;i++) {
			if (arr[i] == '-') {
				error = 1;
			}
		}
		if (error) {
			fprintf(fo, "Case #%d: IMPOSSIBLE\n", t);
		}
		else {
			fprintf(fo, "Case #%d: %d\n", t, sum);
		}
	}
	
	fclose(fo);
	fclose(fi);
	return 0;
}