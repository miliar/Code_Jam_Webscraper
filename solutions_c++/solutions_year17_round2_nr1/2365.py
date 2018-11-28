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

int main() {
	std::ifstream in("cruiseAlarge.in");
	std::ofstream out("cruise.out");

	in >> T;

	for (int i = 0; i < T; i++) {
		double D, N;
		in >> D >> N;

		double maxTimeToComplete = 0;
		for (int j = 0; j < N; j++) {
			double currDistance, currSpeed;
			in >> currDistance >> currSpeed;

			double distanceToGo = D - currDistance;
			double timeToGo = distanceToGo / currSpeed;
			maxTimeToComplete = std::max(maxTimeToComplete, timeToGo);
		}

		out << "Case #" << std::to_string(i + 1) << ": " << std::to_string(D/maxTimeToComplete) << "\n";
	}

	out.close();
	in.close();

}