#include<iostream>
using namespace std;
#include<stdint.h>

bool isSorted(uint64_t n){
	int next_digit = n % 10;
	n = n / 10;
	while (n) {
		int digit = n % 10;
		if (digit > next_digit)
			return false;
		next_digit = digit;
		n = n / 10;
	}
	return true;
}

uint64_t findTidy(uint64_t n) {
	uint64_t lastdigit = 0;
	for (uint64_t i = 0; i <= n; i++){
		if (isSorted(i) == true){
			lastdigit = i;
		}
	}
	return lastdigit;
}

int main() {
	int t;
	cin >> t;
	int k = 1;
	if (t > 0 && t < 101) {
		while (k <= t) {
			uint64_t n;
			cin >> n;
			if (n >= 0 && n < 1001) {
				cout << "Case #" << k << ": " << findTidy(n) << "\n";
			}
			else {
				cout << "Case #" << k << ": " << "0" << "\n";
			}
			k++;
		}
	}
	return 0;
}