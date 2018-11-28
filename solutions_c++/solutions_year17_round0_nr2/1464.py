#include <iostream>
#include <deque>
using namespace std;

void process(deque<int>& digits, __int64 N) {
	//split to digits
	__int64 temp = N;
	while (temp > 0) {
		digits.push_front(temp % 10);
		temp /= 10;
	}
	//
	for (int i = 1; i < digits.size(); ++i) {
		if (digits[i - 1] > digits[i]) {
			for (int j = i, sz = digits.size(); j < sz; ++j) digits[j] = 9;
			int j = i - 1;
			while (j >= 0) {
				--digits[j];
				if (digits[j] < 0) {
					digits[j] = 9;
					--j;
				} else break;
			}
			if (j == 0 && digits[j] == 0) digits.pop_front(); //remove leading zero
			i = j - 1;
			if (i < 0) i = 1;
		}
	}
}

int main() {
	//data
	int T;
	__int64 N;
	
	//input
	cin >> T;

	for (int i = 0; i < T; ++i) {
		// input
		cin >> N;

		//process
		deque<int> digits;
		process(digits, N);

		//output
		cout << "Case #" << (i + 1) << ": ";
		for (int j = 0, sz = digits.size(); j < sz; ++j)
			cout << digits[j];
		if (i + 1 < T) cout << endl;
	}

	return 0;
}