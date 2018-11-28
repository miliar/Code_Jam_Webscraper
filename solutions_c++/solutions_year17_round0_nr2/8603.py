#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
FILE *in = fopen("B-small-attempt0.in", "r");
FILE *out = fopen("output.txt", "w");
long long tidy(long long n) {
	long long arr[1005];
	int i = 0;
	long long sv = n;
	arr[i] = n % 10;
	while (1) {
		n /= 10; i++;
		if (n == 0) break;
		arr[i] = n % 10;
		if (arr[i - 1] < arr[i])
			return tidy(--sv);
	}
	return sv;
}

int main() {
	int t;
	long long n, y;
	fscanf(in,"%d", &t);
	for (int i = 0; i < t; i++) {
		fscanf(in,"%lld", &n);
		y = tidy(n);
		fprintf(out,"Case #%d: %lld\n", i + 1, y);
	}

	return 0;
}