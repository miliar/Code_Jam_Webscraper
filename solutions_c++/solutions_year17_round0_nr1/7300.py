#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	unsigned int		T, test_case = 0, K, minimum_usage;
	std::string			pancakes;

	ifstream	InFile("A-large.in");
	ofstream	OutFile("Test.out", ios_base::ate || ios_base::out);

	if (OutFile.is_open() && InFile.is_open()){
		InFile >> T;

		while (T--){

			InFile >> pancakes >> K;
			minimum_usage = 0;
			auto left_pancake = 0u;
			auto right_pancake = pancakes.size() - 1;

			while (left_pancake <= right_pancake) {

				if ((left_pancake + K) <= pancakes.size()) {
					if (pancakes[left_pancake] == '-') {
						++minimum_usage;
						auto ii = left_pancake;


						for (auto i = 0u; i < K; ++i, ++ii) {
							if (pancakes[ii] == '-')
								pancakes[ii] = '+';
							else
								pancakes[ii] = '-';
						}
					}
				}

				if (right_pancake >= (K - 1)) {
					if (pancakes[right_pancake] == '-') {
						++minimum_usage;

						auto ii = right_pancake;

						for (auto i = 0u; i < K; ++i, --ii) {
							if (pancakes[ii] == '-')
								pancakes[ii] = '+';
							else
								pancakes[ii] = '-';
						}
					}
				}

				++left_pancake;
				--right_pancake;
			}
			
			if (pancakes.find('-') == string::npos)
				OutFile << "Case #" << ++test_case << ": " << minimum_usage << endl;
			else
				OutFile << "Case #" << ++test_case << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
