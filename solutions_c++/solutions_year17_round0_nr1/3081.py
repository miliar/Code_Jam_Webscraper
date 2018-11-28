#include <vector>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

void A(const string &file) {
	ifstream fin(file + ".in");
	ofstream fout(file + ".out");
	int nCases;
	fin >> nCases;
	for (int iCase = 1; iCase <= nCases; ++iCase) {
		fout << "Case #" << iCase << ": ";
		char s[1001];
		int k;
		fin >> s >> k;
		int n = strlen(s);
		char *sign = "+-";
		int x = 1;
		int t = 0;
		int flip[1000] = { 0 };
		int i = 0;
		for (; i < n - k + 1; ++i) {
			if (flip[i]) {
				x = 1 - x;
			}
			if (s[i] == sign[x]) {
				x = 1 - x;
				++t;
				if (i + k < n) {
					flip[i + k] = 1;
				}
			}
		}
		for (; i < n; ++i) {
			if (flip[i]) {
				x = 1 - x;
			}
			if (s[i] == sign[x]) {
				fout << "IMPOSSIBLE" << endl;
				goto ENDCASE;
			}
		}
		fout << t << endl;
	ENDCASE: {}
	}
	fin.close();
	fout.close();
	
	cout << "Done" << endl;
	getchar();
}
