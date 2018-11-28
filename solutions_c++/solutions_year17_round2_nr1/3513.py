#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	int t = 0;
	
	ifstream fin;
	fin.open("A-large.in", ios::in);
	ofstream fout;
	fout.open("output.out", ios::out);

	fin >> t;

	for (int i = 0; i < t; i++) {
		double _max = 0;
		double d = 0, n = 0;
		fin >> d >> n;
		for (int j = 0; j < n; j++) {
			double x = 0, s = 0, k = 0;
			fin >> k >> s;
			x = (d - k) / s;
			if (x > _max) {
				_max = x;
			}
		}
		double res = d / _max;
		cout.precision(6);
		fout << "Case #" << i + 1 << ": " << fixed << res << endl;
		
	}

	return 0;
}