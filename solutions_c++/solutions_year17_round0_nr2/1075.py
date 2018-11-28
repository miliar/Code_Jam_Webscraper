#include <iostream>
using namespace std;

int main() {
	int T;
	string num;

	cin >> T;

	for (int t=1 ; t<=T ; ++t) {
		cin >> num;

		int len = num.length();

		for (int i=len-2 ; i>=0 ; --i) {
			if (num[i] > num[i+1]) {
				num[i+1] = 'x';
				--num[i];
			}
		}

		cout << "Case #" << t << ": ";
	
		bool flag = 0;
		for (int i=0 ; i<len ; ++i) {
			if (flag || num[i] == 'x') {
				flag = 1;
				cout << '9';
			}
			else if (num[i] > '0')
				cout << num[i];
		}

		cout << endl;
	}

	return 0;
}