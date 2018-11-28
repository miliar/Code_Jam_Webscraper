#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <queue>

using namespace std;

long long int n, k;
vector<long long int> a[70], c[70];

int log2(long long int n) {
	int res = 0;
	long long int tmp = n;
	while (tmp > 0) {
		++res;
		tmp /= 2;
	}
	return res;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("stallsl.out", "w", stdout);
	int t; scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		scanf("%lld%lld", &n, &k);
		printf("Case #%d: ", test);
		int lg2 = log2(n);
		for(int i = 0; i <= lg2; i++) a[i].clear(), c[i].clear();
		a[0].push_back(n); 
		c[0].push_back(1);
		long long int pow2;
		for(int i = 0; i <= lg2; i++) {
			int size = a[i].size();
			// cout << size << " ";
			// for(int j = 0; j < size; j++) cout << a[i][j] << " ";
			if (i == 0) pow2 = 0;
			else pow2 = 1LL << (i - 1);
			if (k <= pow2) {
				long long int rmax, rmin;
				if (size == 1) {
					rmax = rmin = a[i][0];
				}
				else {
					if (c[i][0] == c[i][1]) {
						rmax = max(a[i][0], a[i][1]);
						rmin = min(a[i][0], a[i][1]);
					}
					else {
						if (c[i][0] < c[i][1]) {
							rmin = a[i][1];
							if (k <= c[i][0]) {
								rmax = a[i][0];
							}
							else {
								rmax = a[i][1];
							}
						}
						else {
							rmax = a[i][0];
							if (k <= pow2 - c[i][1]) {
								rmin = a[i][0];
							}
							else {
								rmin = a[i][1];
							}
						}
					}
				}
				printf("%lld %lld\n", rmax, rmin);
				break;
			}
			k -= pow2;
			for(int j = 0; j < size; j++) {
				long long int p = a[i][j] / 2;
				long long int q = a[i][j] - 1 - p;
				if (p < q) swap(p, q);
				int posp = -1, posq = -1;
				int stmp = a[i + 1].size();
				for(int h = 0; h < stmp; h++) {
					if (a[i + 1][h] == p) posp = h;
					if (a[i + 1][h] == q) posq = h;
				}
				if (p == q) {
					if (posp == -1) {
						a[i + 1].push_back(p);
						c[i + 1].push_back(c[i][j] * 2);
					}
					else {
						c[i + 1][posp] += c[i][j] * 2;
					}
				}
				else {
					if (posp == -1) {
						a[i + 1].push_back(p);
						c[i + 1].push_back(c[i][j]);	
					}
					else {
						c[i + 1][posp] += c[i][j];
					}
					if (posq == -1) {
						a[i + 1].push_back(q);
						c[i + 1].push_back(c[i][j]);	
					}
					else {
						c[i + 1][posq] += c[i][j];
					}
				}
			}
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}