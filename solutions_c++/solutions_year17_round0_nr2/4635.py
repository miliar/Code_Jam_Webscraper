#include <algorithm>
#include <bitset>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int tc = 1; tc <= t; tc++) {
		string num;
		cin >> num;

		for (size_t i = 1; i < num.length(); i++) {
			if (num[i] < num[i - 1]) {
				for (size_t j = i - 1;; j--) {
					--num[j];

					if (j == 0 || num[j - 1] <= num[j])
						break;

					num[j] = '9';
				}
				for (size_t j = i; j < num.length(); j++) {
					num[j] = '9';
				}

				break;
			}
		}

		if (num[0] == '0')
			num.erase(0, 1);

		cout << "Case #" << tc << ": " << num << endl;
	}
}
