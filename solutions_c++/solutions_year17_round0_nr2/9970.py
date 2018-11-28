#include <stdio.h>

int findTidy(int arr[]) {
	for (int i = 1; arr[i] != -1; i++)
		if (arr[i] > arr[i - 1])
			return 0;
	return 1;
}

int intToArr(int n) {
	int res, i = 0, arr[] = {-1, - 1, - 1, -1}, temp = n;
	while (n) {
		arr[i++] = n % 10;
		n /= 10;
	}
	return findTidy(arr) ? temp : 0;
}

int main() {
	int n, t;
	FILE* fp = fopen("B-small-attempt1.in", "r");
	FILE* fp2 = fopen("B-small-attempt1.out", "w");

	fscanf(fp, "%d", &t);

	for (int i = 0; i < t; i++) {
		fscanf(fp, "%d", &n);
		int res = intToArr(n);
		while (!res)
			res = intToArr(--n);
		fprintf(fp2, "Case #%d: %d\n", i + 1, res);
	}
	fclose(fp);

	return 0;
}