#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[]) {
	if (argc <= 1)
		return -1;

	std::ifstream input_file;
	std::ofstream output_file("output");

	input_file.open(argv[1]);

	int T;
	input_file >> T;
	for (int t = 1; t <= T; t++) {
		std::string N, M;
		
		input_file >> N;
		M = N.back();

		for (int i = N.length() - 2; i >= 0; i--) {
			if (N[i] <= M[0]) {
				M = N[i] + M;
			}
			else {
				M = (char)(N[i] - 1) + std::string((size_t)M.length(), '9');
			}
		}

		if (M[0] == '0')
			M.erase(0, 1);

		output_file << "Case #" << t << ": "
			        << M << std::endl;
	}

	return 0;
}