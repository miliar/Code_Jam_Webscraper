#include <iostream>
#include <fstream>
#include <iomanip>

int main(int argc, char* argv[]) {
	if (argc < 2) {
		std::cout << "No input file" << std::endl;
		return 0;
	}

	std::ifstream input_file(argv[1]);
	std::ofstream output_file("output");

	if (!input_file.is_open()) {
		std::cout << "Failed to open" << std::cout;
		return 0;
	}


	int T;
	input_file >> T;

	output_file << std::fixed << std::setprecision(6);

	for (int t = 1; t <= T; t++) {
		long long D, N;
		double result = -1;
		input_file >> D;
		input_file >> N;

		long long* K = new long long[N];
		long long* S = new long long[N];

		for (int n = 0; n < N; n++) {
			input_file >> K[n];
			input_file >> S[n];
		}

		for (int n = 0; n < N; n++) {
			double time = (D - K[n]) / (double) S[n];
			if (time > result || result < 0) {
				result = time;
			}
		}

		output_file << "Case #" << t << ": "
		            << D / result << std::endl;
	}

	return 1;
}