#include <iostream>
using namespace std;

string solve() {
	string s;

	cin >> s;
	int len = s.length();

	int a[19];

	for (int i = 0; i < len; i++) {
		a[i] = s.at(i) - '0';
	}

	for (int i = 1; i < len; i++) {
		int index = len - i;
		int next_index = index - 1;
		
		if (a[index] < a[next_index]) {

			a[next_index] --;
			for (int j = index; j < len; j++) {
				a[j] = 9;
			}
		}
	}

	int zero_skip = true;

	char buf[20];
	int index = 0;
	for (int i = 0; i < len; i++) {
		if (zero_skip && a[i] == 0) {
			continue;
		}
		buf[index] = (char) (a[i] + '0');
		index++;
		zero_skip = false;
	}
	if (index == 0) {
		buf[0] = '0';
		index++;
	}
	buf[index] = (char) 0;


	return string(buf);
}


int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		string result = solve();

		cout << "Case #" << i + 1 << ": "; 
		cout << result << endl;

	}


	return 0;
}
