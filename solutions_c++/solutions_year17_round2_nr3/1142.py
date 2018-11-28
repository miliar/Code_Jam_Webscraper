#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

int main() {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		int n, q;
		fin >> n >> q;

		vector<pair<int, int>> horses;

		for (int i = 0; i < n; i++) {
			int e, s;
			fin >> e >> s;
			horses.push_back(make_pair(e, s));
		}

		vector<int> distances; //distances[i] is the distance from i to i+1

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				//ignoring this for small dataset
				int d;
				fin >> d;
				if (d != -1) {
					distances.push_back(d);
				}
			}
		}

		//small dataset, only 1 line here
		int u, v;
		fin >> u >> v;

		vector<double> quickest(n, 0.0);

		for (int i = n - 2; i >= 0; i--) {
			//calculate fastest from this city starting from second right city
			double m = -1.0;
			int d = 0;
			for (int j = i + 1; j < n; j++) {
				d += distances[j - 1];
				if (d <= horses[i].first) {
					double time = (double)d / (double)horses[i].second + quickest[j];
					if (m < 0 || time < m) m = time;
				}
				else {
					break;
				}
			}
			quickest[i] = m;
		}

		fout << "Case #" << to_string(t) << fixed << setprecision(9) << ": " << quickest[0] << endl;
	}
	fout.close();
	return 0;
}