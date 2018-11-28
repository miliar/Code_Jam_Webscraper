#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

#include <stdio.h>
#include <string.h>
int a[10000];



int main() {
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int t;
	long long int n;
	
	long long int k;
	long long int l;
	long long int r;
	fscanf(in, "%d", &t);
	for (int T=1; T <= t; T++) {
		fscanf(in, "%lld %lld", &n, &k);
		while (k != 0) {
			l = (n - 1) / 2;
			r = n / 2;
			if (k % 2 == 0) {
				n = r;
			}
			else {
				n = l;
			}
			k /= 2;

		}
		if (l > r) {
			fprintf(out, "Case #%d: %lld %lld\n", T, l, r);
		}
		else {
			fprintf(out, "Case #%d: %lld %lld\n", T, r, l);
		}
	}
	return 0;
}