#include <iostream>
//#include "stdio.h"
#include <string>
using namespace std;


int main() {
	int t;
	cin >> t;

	int r,c;
	string s[30];
	bool allm[30];
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> r >> c;
		for (int i = 0; i < r; ++i) {
			cin >> s[i];
			allm[i] = false;
		}
		cout << "Case #" << tcount << ": \n";

		for (int i = 0; i < r; ++i) {
			int pt = 0;
			while (s[i][pt] == '?' && pt < c)
				++pt;
			if (pt >= c) {
				allm[i] = true;
			}
			else {
				for (int j = 0; j < pt; ++j)
					s[i][j] = s[i][pt];

				for (int j = pt + 1; j < c; ++j)
					if (s[i][j] == '?')
						s[i][j] = s[i][pt];
					else
						pt = j;
			}

			//cout << s[i] << endl;
		}
		for (int i = 0; i < r; ++i) {
			if (!allm[i])
				goto thisforend;

			for (int j = 1; j < r; ++j) {
				if (i + j < r && !allm[i + j]) {
					s[i] = s[i + j];
					goto thisforend;
				}
				if (i - j >= 0 && !allm[i - j]) {
					s[i] = s[i - j];
					goto thisforend;
				}
			}

		thisforend:
			cout << s[i] << endl;
		}
	}

	return 0;
}