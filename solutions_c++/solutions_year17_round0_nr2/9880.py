#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;

int compare(const void * x1, const void * x2)
{
	return (*(int*)x1 - *(int*)x2);
}

int main() {
	std::ios::sync_with_stdio(false);

	ifstream fin("B-small-attempt0.in");
	ofstream fout("output");

	int T;
	fin >> T;
	for (int e = 0; e < T; ++e) {
		fout << "Case #" << e + 1 << ": ";
		long long q;
		fin >> q;
		int a[18];
		for (int i = 17; i >= 0; --i) {
			a[i] = q % 10;
			q /= 10;
		}
		int i = 0;
		while (i < 17 && a[i] <= a[i + 1]) {
			++i;
		}
		if (i != 17) {
			--a[i];
			int j = i;
			while (j > 0 && a[j] < a[j - 1]) {
				a[j] = 9;
				--a[j-- - 1];
			}
			++i;
			while (i < 18) {
				a[i++] = 9;
			}
		}
		bool f = false;
			for (int j = 0; j < 18; ++j) {
				if (a[j] || f) {
					f = true;
					fout << a[j];
				}
			}

		fout << endl;
	}

	fin.close();
	fout.close();

	return 0;
}