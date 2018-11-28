#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cfloat>
#include <iostream>
#include <algorithm>
#include <climits>
#include <set>
#include <map>

int T;
double N, K;

int main() {
	std::ifstream in("C-small-2-attempt0.in");
	std::ofstream out("stalls.out");

	in >> T;
	for (int i = 0; i < T; i++) {
		std::map<double, double> splits;
		std::map<double, double>::iterator it;

		in >> N >> K;

		double splitsDone = 0;
		bool isOver = false;

		splits[N] = 1;
		while (!isOver) {
			double gapSize = splits.rbegin()->first - 1;
			double numGaps = splits.rbegin()->second;

			splitsDone += numGaps;

			if (splitsDone >= K) { //its over, tell them what they want
				out << "Case #" << std::to_string(i + 1) << ": " << std::to_string((int)(gapSize - floor(gapSize / 2))) << " " << std::to_string((int)(floor(gapSize / 2))) << "\n";
				splits.clear();
				isOver = true;
				break;
			}
			else {
				splits[floor(gapSize / 2)] += numGaps;
				splits[gapSize - floor(gapSize / 2)] += numGaps;
				splits.erase(splits.rbegin()->first);
			}

		}
	}

}