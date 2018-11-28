#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		int d, n;
		fin >> d >> n;
		vector<pair<int, int>> horses;
		for (int i = 0; i < n; i++) {
			int k, s;
			fin >> k >> s;
			horses.push_back(make_pair(k, s));
		}

		double max = -1;

		for (auto horse : horses) {
			int dist = d - horse.first;
			double time = (double)dist / (double)horse.second;
			if (max < 0) max = time;
			else if (time > max) max = time;
		}

		double answer = (double)d / max;

		fout << "Case #" << to_string(t) << fixed << setprecision(9) << ": " << answer << endl;
	}
	fout.close();
	return 0;
}