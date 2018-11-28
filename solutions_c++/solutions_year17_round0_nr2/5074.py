#include <iostream>
#include <string>
#include <vector>

using namespace std;

static_assert(sizeof(size_t) == 8, "asd");

int main() {
	int t;
	cin >> t;
	for (int it = 1; it <= t; ++it) {
		std::string num;
		cin >> num;

		string maxTidy;
		char max = '0';
		bool isFilling9 = false;
		for (char c : num) {
			if (isFilling9) {
				maxTidy.push_back('9');
				continue;
			}

			if (c >= max) {
				maxTidy.push_back(c);
				max = c;
				continue;
			}

			int numPops = 0;
			while (maxTidy.length() > 0 && maxTidy.back() == max) {
				maxTidy.pop_back();
				++numPops;
			}

			if (max > '1') {
				maxTidy.push_back(max - 1);
			}

			isFilling9 = true;
			for (int i = 0; i < numPops; ++i)
				maxTidy.push_back('9');
		}

		cout << "Case #" << it << ": " << maxTidy << endl;
		cout.flush();
	}
}