#include <iostream>
#include <map>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int case_counter = 1; case_counter <= cases; case_counter++) {

		string str;
		cin >> str;

		int first_equal = 0;
		int i;
		for (i = 1; i < str.length(); i++) {
			if (str[i - 1] < str[i]) {
				first_equal = i;
			} else if (str[i - 1] > str[i]) {
				break;
			}
		}

		if (i < str.length()) {

			str[first_equal] = str[first_equal] - 1;

			for (int j = first_equal + 1; j < str.length(); j++)
				str[j] = '9';

			if (str[0] == '0')
				str = str.substr(1);
		}

		cout << "Case #" << case_counter << ": " << str << endl;

	}
	return 0;
}
