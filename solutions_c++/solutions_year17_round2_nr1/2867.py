#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;
int main() {
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int k;
	in >> k;
	out.setf(std::ios::fixed);
	out.precision(6);
	for (int i = 1; i <= k; i++) {
		vector<pair<int, int>> hrs;
		int d, n;
		int tmp1, tmp2;
		double time = 0;
		in >> d >> n;
		for (int j = 0; j < n; j++) {
			in >> tmp1 >> tmp2;
			if ((d - tmp1) / (double)tmp2 > time)
				time = (d - tmp1) / (double)tmp2;
		}
		out << "Case #" << i << ": " << (double)d / time << endl;
	}
	return 0;
}