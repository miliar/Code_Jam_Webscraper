#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
	if (argc <= 1)
		return -1;

	std::ifstream input_file;
	std::ofstream output_file("output");

	input_file.open(argv[1]);

	int T;
	input_file >> T;
	for (int t = 1; t <= T; t++) {
		long long int N, K;
		input_file >> N;
		input_file >> K;

		long long int k = K;
		long long int l = 1;

		while (k > 1) {
			l <<= 1;
			k >>= 1;
		}

		k = K - l + 1;

		long long int slot = (N - l + 1) / l;
		long long int ex = (N - l + 1) % l;

		if (k <= ex)
			slot++;

		long long int min, max;
		max = slot / 2;
		min = slot & 1 ? max : max - 1;

		output_file << "Case #" << t << ": ";
		output_file << max << ' ' << min << std::endl;
	}

	return 0;
}