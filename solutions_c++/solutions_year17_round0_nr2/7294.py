#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	unsigned int		T, test_case = 0;
	std::string			pancakes;

	ifstream	InFile("B-large.in");
	ofstream	OutFile("Test.out", ios_base::ate || ios_base::out);

	if (OutFile.is_open() && InFile.is_open()) {
		InFile >> T;

		while (T--) {
			string N;
			InFile >> N;
			auto current_index = 1u;

			while (current_index < N.size()) {
				if (N[current_index] < N[current_index - 1])
					break;
				++current_index;
			}

			if (current_index < N.size()) {
				--current_index;
				for (auto i = 0u; i < current_index; ++i) {
					if (N[i] > N[current_index] - 1) {
						current_index = i;
						break;
					}
				}

				N[current_index] = N[current_index] - 1;

				for (++current_index; current_index < N.size(); ++current_index)
					N[current_index] = '9';

				current_index = 0;

				while (N[current_index] == '0')
					++current_index;

				if (current_index != 0)
					N = N.substr(current_index);
			}
			
			OutFile << "Case #" << ++test_case << ": " << N << endl;
		}
	}

	return 0;
}