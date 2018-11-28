#include <iostream>
#include <string>
#include <cmath>

using namespace std;

bool istidy(long long n) {	
	int digit = n % 10;
	n /= 10;
	while (n>0) {
		if (n % 10 > digit) return false;
		digit = n % 10;
		n /= 10;
	}
	return true;
}

string doCase() {
	long long n;
	cin >> n;
	int len = to_string(n).length();

	string ans;
	for (int i=0; i<len; i++) {
		if (istidy(n)) {
			if (n>0) ans = to_string(n) + ans;
			return ans;
		} else {
			ans = "9" + ans;
			n /= 10;
			n--;
		}
	}
	return "error";
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) cout << "Case #" << i+1 << ": " << doCase() << endl;
	return 0;
}