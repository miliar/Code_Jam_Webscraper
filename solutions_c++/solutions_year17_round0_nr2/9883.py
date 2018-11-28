#include <iostream>

#define BASE	10
#define MAX		19

using namespace std;

int main () {
	int T;
	int digits[MAX];
	signed long long int N, i, last_non_decreasing, length;
	
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> N;
		// read N into array; the least significant digits at the lowest indices
		i = 0;
		while (N > 0) {
			digits[i] = (N % BASE);
			N /= BASE;
			++i;
		}
		length = i;
		
		if (length > 1) {
			i = length - 1;
			// find first decreasing subsequence
			while (i > 0 && digits[i] <= digits[i - 1]) --i;
			last_non_decreasing = i;
			
			if (last_non_decreasing > 0) {
				// subtract 1 from digits[last_non_decreasing..length-1]
				do {
					if (digits[i - 1] == 0) digits[i - 1] = 9;
					--digits[i]; 
					++i;
				} while (i < length && digits[i] > digits[i - 1]);

				
				// fill up the rest of the number (digits[0..last_non_decreasing-1]) with 9s
				i = last_non_decreasing - 1;
				while (i >= 0) {
					digits[i] = 9;
					--i;
				}
			}
		}
		
		cout << "Case #" << t << ": ";
		// get rid of leading 0s
		while (digits[length - 1] == 0) --length;
		for (i = length; i > 0; --i) {
			cout << digits[i - 1];
		}
		cout << endl;
	}
	
	return 0;
}
