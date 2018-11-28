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
	freopen("H:\\Projects\\Codejam2017\\b_in.txt", "r", stdin);
	freopen("H:\\Projects\\Codejam2017\\b_out.txt", "w", stdout);

	string s;
	const int MAXN = 4;
	char ch;
	int tests, test, n, m, x, y;
	double C, F, X;
	int D = 0;
	int N, R, O, Y, G, B, V;

	scanf("%d", &tests);

	for (test = 1; test <= tests; ++test) {
		cin >> N >> R >> O >> Y >> G >> B >> V;
		string ans = ""; 
		
		char first = ' '; 
		char selected = ' '; 
		char prev = ' '; 
		for (int i = 0; i < N; ++i) {
			int M = max(R, max(Y, B)); 
			if (M == 0) {
				ans = "IMPOSSIBLE";
				break;
			}
			selected = ' '; 
			if (                   M == R && 'R' != prev) selected = 'R';
			if (selected == ' ' && M == Y && 'Y' != prev) selected = 'Y';
			if (selected == ' ' && M == B && 'B' != prev) selected = 'B';

			if (selected != ' ' && M == Y && 'Y' != prev && 'Y' == first) selected = 'Y';
			if (selected != ' ' && M == B && 'B' != prev && 'B' == first) selected = 'B';

			if (selected == ' ') {
				int selectedNum = 0;
				if ('R' != prev && R > selectedNum) { selected = 'R'; selectedNum = R; }
				if ('Y' != prev && Y > selectedNum) { selected = 'Y'; selectedNum = Y; }
				if ('B' != prev && B > selectedNum) { selected = 'B'; selectedNum = B; }
			}

			if (selected == ' ') {
				ans = "IMPOSSIBLE"; 
				break; 
			} else {
				if (i == 0) first = selected;
				ans += selected; 
				prev = selected; 
				if (selected == 'R') --R;
				if (selected == 'Y') --Y;
				if (selected == 'B') --B;
			}
		}
		if (prev == first && N > 2) ans = "IMPOSSIBLE";
		// as for small
		printf("Case #%d: %s\n", test, ans.c_str());
	}

	return 0;
}
