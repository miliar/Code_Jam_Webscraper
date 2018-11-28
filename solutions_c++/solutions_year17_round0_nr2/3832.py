#include <iostream>
#include <string>

#define ull unsigned long long

using namespace std;


string getLastTidy(string digits) {
	for(int i = 0; i < digits.length()-1; i++) {
		int cur = digits.length()-2-i;
		if(digits[cur] > digits[cur+1]) {
			digits[cur] = digits[cur]-1;
			for(int j = cur+1; j < digits.length(); j++) {
				digits[j] = '9';
			}
		}
	}

	int first = 0;
	for(int i = 0; i < digits.length(); i++) {
		if(digits[i] != '0') {
			first = i;
			break;
		}
	}
	digits = digits.substr(first, digits.length()-first);

	return digits;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	string N;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> N;
		cout << "Case #" << (i+1) << ": " << getLastTidy(N) << endl;
	}

	return 0;
}
