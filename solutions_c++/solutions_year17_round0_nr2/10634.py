#include <bits/stdc++.h>

using namespace std;
int main() {
	ifstream fin("file.in");
	ofstream fout("out.out");

	int t; fin >> t;
	for (int z = 1; z <= t; ++z) {
		fout << "Case #" << z << ": ";
		int n; fin >> n;
		for (int i = n; i > 0; --i) {
			int digits = log10(i);
			int digit1 = i / (int)pow(10, digits);
			int j;
			for (j = digits -1; j >= 0; --j) {
				int digit = i / (int)pow(10, j);
				digit = digit % 10;
				if (digit1 > digit) break;
				digit1 = digit;
			}
			if (j == -1) {
				fout << i << endl;
				break;
			}
		}
	}
	fin.close();
	fout.close();
}
