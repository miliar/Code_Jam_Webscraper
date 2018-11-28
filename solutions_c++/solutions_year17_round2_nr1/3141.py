#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

struct Horse {
	int64_t position;
	int speed;
};

void solve(int testCase, ifstream &input, ofstream &output) {
	int64_t d, n;

	input >> d >> n;
	Horse horses[n];

	for (int i = 0; i < n; i++) {
		input >> horses[i].position >> horses[i].speed;
	}

	double maxTime = 0;

	for (int i = n - 1; i >= 0; i--) {
		double time = (double) (d - horses[i].position) / horses[i].speed;

		if (time > maxTime) maxTime = time;
	}

	output << "Case #" << testCase << ": " << fixed << setprecision(6) << (double) d / maxTime << endl;
}

int main(int argc, char *argv[]) {
	if (argc > 0) {
		ofstream outputFile(argv[2]);
		ifstream inputFile(argv[1]);

		int t;
		inputFile >> t;

		for (int i = 0; i < t; i++) {
			cout << "Solving case " << i + 1 << endl;

			solve(i + 1, inputFile, outputFile);
		}
	}

	return 0;
}