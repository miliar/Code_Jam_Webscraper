#include <iostream>
#include <algorithm>
//#include "stdio.h"
#include <string>
using namespace std;


int main() {
	int t;
	cin >> t;

	int n, p;
	int r[60];
	int q[60][60];
	int mi[60][60];
	int ma[60][60];
	int pt[60];
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> n >> p;
		for (int i = 0; i < n; ++i) {
			cin >> r[i];
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < p; ++j)
				cin >> q[i][j];
			sort(q[i], q[i] + p);
			for (int j = 0; j < p; ++j) {
				ma[i][j] = floor((double)(q[i][j]) / (double)(r[i]) / 0.9);
				mi[i][j] = ceil((double)(q[i][j]) / (double)(r[i]) / 1.1);
			}
			pt[i] = p - 1;
		}
		cout << "Case #" << tcount << ": ";

		int count = 0;
		//int mmi = 0, mma = 1000000;
		while (true) {
			int mmi = 0, mma = 1000000;
			for (int i = 0; i < n; ++i) {
				if (pt[i] < 0)
					goto thisend;
				if (mmi < mi[i][pt[i]])
					mmi = mi[i][pt[i]];
				if (mma > ma[i][pt[i]])
					mma = ma[i][pt[i]];
			}
			if (mmi > mma) {
				for (int i = 0; i < n; ++i)
					if (mi[i][pt[i]] == mmi)
						pt[i] --;
			}
			else {
				++count;
				for (int i = 0; i < n; ++i)
					pt[i] --;
			}
		}

	thisend:
		cout << count << endl;
	}

	return 0;
}