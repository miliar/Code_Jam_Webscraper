#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text



long long correct(long long n) {
	if (n < 10) return n;
	long long ans = n;


	int nDigits = 0;

	long long mod = 1;
	while (ans) {
		nDigits++;
		ans /= 10;
		mod = mod * 10;
	}
	mod /= 10;
	ans = 0;

	int curDigit = 0;
	int nextDigit = 0;
	for (int i = 0; i < nDigits - 1; i++) {
		curDigit = (n / mod) % 10;
		nextDigit = (n / (mod/(long long)10)) % 10;

		if (nextDigit < curDigit) {
			ans = ans * 10 + curDigit - 1;
			ans = ans * (mod/(long long)10) + ((mod/(long long)10) - 1);
			nextDigit = 9;
			break;
		}
		ans = ans * (long long)10 + curDigit;
		mod /= (long long)10;
	}

	ans = ans * (long long)10 + nextDigit;





	return ans;
}


void main() {
	int t;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int testCase = 1; testCase <= t; ++testCase) {
		long long N;
		cin >> N;

		for (int i = 0; i < 20; i++) {
			N = correct(N);
		}
		


		cout << "Case #" << testCase << ": " << N << endl;

	}
}
