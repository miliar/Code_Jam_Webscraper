#include <iostream>
#include <iomanip>

using namespace std;


int main(int argc, char* argv[]) {


	int testCases = 0;
	cin >> testCases;

	for (int i = 0; i < testCases; i++) {

		unsigned long long destination;
		unsigned int cantHorses;
		cin >> destination >> cantHorses;

		double maxTime = 0;
		for (int i = 0; i < cantHorses; ++i) {
			unsigned long long ik;
			unsigned int s;
			cin >> ik >> s;

			unsigned long long distance = destination - ik;
			double time = distance / (double) s;

			if (time > maxTime)
				maxTime = time;

		}

		cout << std::fixed;
		cout << std::setprecision(6);
		cout << "Case #" << i + 1 << ": " << (destination / ((double) maxTime)) << endl;

	}
}