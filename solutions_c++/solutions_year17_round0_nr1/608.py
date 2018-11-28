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
		std::string row;
		int K;

		input_file >> row;
		input_file >> K;

		int flips = 0;
		bool posible = true;
		int i;
		for (i = 0; i < row.length() - K + 1; i++) {
			if (row[i] == '-') {
				flips++;
				for (int n = i; n < i + K; n++) {
					row[n] = row[n] == '+' ? '-' : '+';
				}
			}
		}

		for (; i < row.length(); i++) {
			if (row[i] == '-') {
				posible = false;
				break;
			}
		}


		output_file << "Case #" << t << ": ";

		if (posible)
			output_file << flips << std::endl;
		else
			output_file << "IMPOSSIBLE" << std::endl;
	}

	return 0;
}