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
#include <iomanip>
#include <sstream>

int T;
int K, S;

int main() {
	std::ifstream in("A-large.in");
	std::ofstream out("pancakes.out");

	in >> T;
	for (int i = 0; i < T; i++) {
		std::string pancakes;
		std::vector<bool> pancks;
		in >> pancakes >> K;

		int flips = 0;

		for (int m = 0; m < pancakes.length(); m++) {
			if (pancakes[m] == '+') {
				pancks.push_back(true);
			}
			else {
				pancks.push_back(false);
			}
		}

		S = pancks.size();
		for (int j = 0; j < S - (K-1); j++) {
			if (!pancks[j]) {
				flips++;
				for (int k = 0; k < K; k++) {
					pancks[j + k] = !pancks[j + k];
				}
			}
		}

		bool wasPossible = true;
		for (int j = 0; j < pancks.size(); j++) {
			if (!pancks[j]) wasPossible = false;
		}

		if (wasPossible) {
			out << "Case #" << std::to_string(i + 1) << ": " << std::to_string(flips) << "\n";
		}
		else {
			out << "Case #" << std::to_string(i + 1) << ": IMPOSSIBLE\n";
		}

	}

}