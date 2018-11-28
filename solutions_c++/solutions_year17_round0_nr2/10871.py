#include <iostream>
#include <fstream>
#include <vector>

int main(int argc, char **argv)
{
	std::ifstream input("D:\\B-small-attempt2.in");
	std::ofstream output("D:\\output.out");

	short T = 0;
	input >> T;

	for (short i = 1; i <= T; ++i) {
		unsigned N = 0;
		input >> N;
		int last = 1;

		for (unsigned j = 1; j <= N; ++j) {
			unsigned n = j;
			std::vector<unsigned> v;

			while (n) {
				v.push_back(n % 10);
				n /= 10;
			}

			unsigned new_last = v[0];
			bool good = true;
			for (auto k = 1; k < v.size(); ++k) {
				if (v[k - 1] < v[k]) {
					good = false;
					break;
				} else {
					new_last += pow(10, k) * v[k];
				}
			}

			if (good) {
				last = new_last;
			}
		}
		output << "Case #" << i << ": " << last << "\n";
	}

	input.close();
	output.close();
	return 0;
}
