#include <iostream>
#include <fstream>

char color[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int max(int* list, int ex = -1, int p = -1, int n = 6) {
	int m = 0;
	int r;
	for (int i = 0; i < n; i++) {
		if (i == ex)
			continue;
		if (list[i] > m) {
			m = list[i];
			r = i;
		}
		if (list[i] == m && i == p) {
			m = list[i];
			r = i;
		}
	}
	return r;
}


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

	for (int t = 1; t <= T; t++) {
		int N;
		int n[6];

		bool posible = true;
		std::string result;

		input_file >> N;
		input_file >> n[0];
		input_file >> n[1];
		input_file >> n[2];
		input_file >> n[3];
		input_file >> n[4];
		input_file >> n[5];

		if (2 * n[max(n)] > N) {
			posible = false;
		}

		if (posible) {
			int k = -1;
			int first = max(n, k);

			for (int i = 0; i < N; i++) {
				k = max(n, k, first);
				result += color[k];
				n[k]--;
			}
		}

		output_file << "Case #" << t << ": ";
		if (posible)
			output_file << result << std::endl;
		else
			output_file << "IMPOSSIBLE" << std::endl;
	}

	return 1;
}