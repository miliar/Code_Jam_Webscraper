#include <cmath>
#include <ctgmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <ctgmath>
#include <fstream>
using namespace std;

#define MAXN 400


int t, k;
string s;

ifstream fin ("1.in");
ofstream fout ("1.out");

int main() {

	fin >> t;

	for (int a = 0; a < t; a++) {
		int val = 0;
		fin >> s;
		fin >> k;


		for (int i = 0; i <= (int)s.length() - k; i++) {

			if (s[i] == '-') {
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
				val++;
			}
		}

		bool flag = 0;

		for (int i = (int)s.length() - k; i < (int)s.length(); i++) {
			if (s[i] == '-') flag = 1;
		}
		if (flag) {
			fout << "Case #" << a + 1 << ": IMPOSSIBLE" << endl;
		}
		else {
			fout << "Case #" << a+1 << ": " << val << endl;
		}

	}

    fin.close();
    fout.close();

	return 0;
}
