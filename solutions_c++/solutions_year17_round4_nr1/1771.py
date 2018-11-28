#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <numeric>
#include <algorithm>
#include <vector>
#include <map>
#include <random>
#include <cstdio>
#include <cmath>
using namespace std;


int main() {

	string s;
	const int MAXN = 4;
	char ch;
	int tests, test, n, m, x, y;
	double C, F, X;
	int D;
	int N, P;
	vector<pair<int, int>> horses;

	freopen("H:\\Projects\\Codejam2017R2\\a.in.txt", "r", stdin);
	freopen("H:\\Projects\\Codejam2017R2\\a.out.txt", "w", stdout);

	scanf("%d", &tests);

	for (test = 1; test <= tests; ++test) {
		scanf("%d %d", &N, &P);
		vector<int> groups = vector<int>(N, 0);


		for (int i = 0; i < N; ++i) {
			scanf("%d", &groups[i]);
		}

		int leftover = 0; 

		if (P == 2) {
			int odds = 0; 
			for (int i = 0; i < N; ++i) if (groups[i] % 2 == 1) ++odds; 
			leftover = (odds >> 1);
		} else 
		if (P == 3) {
			int o31 = 0; 
			int o32 = 0; 
			for (int i = 0; i < N; ++i) {
				if (groups[i] % 3 == 1) {
					++o31; 
				} else 
				if (groups[i] % 3 == 2) {
					++o32; 
				}
			}

			leftover = min(o31, o32); 
			o31 -= leftover; 
			o32 -= leftover; 
			int om = max(o31, o32); 
			if (om > 0) {
				int gs = (int)floor(om / 3);
				int left = (om % 3 == 2) ? 1 : 0;
				leftover += gs * 2 + left; 
			}
		}


		printf("Case #%d: %d\n", test, N - leftover);
	}

	return 0;
}
