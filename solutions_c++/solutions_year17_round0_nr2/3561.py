#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

#define MAXN 1005

using namespace std;

int tt;

bool tidy(int a) {
	int b = 10;
	while (a > 0) {
		if (a % 10 > b) return false;
		b = a % 10;
		a /= 10;
	}
	return true;
}

int main() {
	FILE *fout, *fin;
	fout = fopen("bout.txt", "wb");
	fin = fopen("B-small-attempt0.in", "r");
	fscanf(fin, "%d", &tt);
	for (int t = 1 ; t <= tt ; t ++) {
		int n;
		fscanf(fin, "%d", &n);
		for (; !tidy(n) ; n --) {}
		fprintf(fout, "Case #%d: %d\n", t, n);
	}
	fclose(fout);
	return 0;
}