#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	
	int t;
	char num[20];

	cin >> t;

	for (int i = 1; i <= t; i++) {

		cin >> num;

		int len = strlen(num);
		int last9 = len;
		int firstNon0 = 0;

		if (len == 1) {
			
			cout << "Case #" << i << ": " << num << "\n";
			continue;
		}

		for (int j = len - 2; j >= 0; j-- ) {

			if (num[j] > num[j + 1]) {

				last9 = j + 1;
				num[j] = num[j] - 1;
			}
		}

		cout << "Case #" << i << ": ";

		for (int j = 0; j < len ; j++) {

			if (firstNon0 == 0 && num[j] == '0' && last9 > j) {
				continue;
			}

			if (num[j] != '0') {
				firstNon0 = 1;
			}

			if (j < last9) {

				cout << num[j];
			} else {

				cout << "9";
			}
		}

		cout << "\n";
	}

	return 0;
}