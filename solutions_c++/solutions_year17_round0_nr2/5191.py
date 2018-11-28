#include <iostream>
#include <vector>
#include <string>

using std::cin;
using std::cout;
using std::endl;

int main()
{
	unsigned T;
	cin >> T;
	cin.get();
	for (unsigned case_num = 1; case_num <= T; ++case_num) {
		std::string line;
		getline(cin, line);

		std::vector<int> limits;

		for (char c : line) {
			limits.push_back(c - '0');
		}

		std::vector<int> res(limits.size(), 0);

		for (size_t i = 0; i != limits.size(); ++i) {
			int min = (i == 0 ? 0 : res[i - 1]);

			if (limits[i] >= min) {
				min = limits[i];
				res[i] = limits[i];
			}
			else {
				for (auto j = i; j != limits.size(); ++j)
					limits[j] = 9;
				limits[i - 1] -= 1;
				res[i - 1] = 0;
				i -= 2;
			}
		}

		unsigned long long res_num = 0, base = 1;
		for (auto iter = res.crbegin(), end = res.crend();
			iter != end; ++iter) {
			res_num += *iter * base;
			base *= 10;
		}

		cout << "Case #" << case_num << ": " << res_num;

		cout << endl;
	}
	return 0;
}
