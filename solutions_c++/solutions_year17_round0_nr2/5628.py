#include <iostream>
#include <string>


using namespace std;

int main() {

	long long testcasenumber;
	cin >> testcasenumber;

	for (long long test = 1; test <= testcasenumber; test++) {

		string sayi;
		cin >> sayi;

		int len = sayi.length();

		for (int i = len - 1; i >= 1; i--) {
			char last_one = sayi[i];
			char last_two = sayi[i - 1];

			if (last_one < last_two) {
				if (last_two == 0) {
					sayi[i - 1] = '9';
				}
				else {
					sayi[i - 1]--;
					for (int j = i; j < len; j++) {
						sayi[j] = '9';
					}
				}
			}
		}

		//if (sayi[0] == '0')
		//sayi = sayi.substr(1);

		cout << "Case #" << test << ": " << atoll(sayi.c_str()) << endl;

	}

	

	return 0;
}