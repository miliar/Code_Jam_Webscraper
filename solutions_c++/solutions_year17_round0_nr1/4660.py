#include <iostream>
#include <bitset>
#include <string>
#include <algorithm>
#include <boost/dynamic_bitset.hpp>

using namespace std;
using namespace boost;

int main()
{
	int t;
	cin >> t;

	for (int tc = 1; tc <= t; tc++) {
		string str;
		cin >> str;

		int k;
		cin >> k;

		boost::dynamic_bitset<> bs(str.length(), 0);
		for (size_t i = 0; i < str.length(); i++) {
			if (str[i] == '+') {
				bs.set(i);
			}
		}

		int flips = 0;

		for (size_t i = 0; i + k <= bs.size(); i++) {
			if (!bs.test(i)) {
				++flips;
				for (int j = 0; j < k; j++) {
					bs.flip(i + j);
				}
			}
		}

		if (bs.all()) {
			cout << "Case #" << tc << ": " << flips << endl;
		} else {
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		}
	}
}
