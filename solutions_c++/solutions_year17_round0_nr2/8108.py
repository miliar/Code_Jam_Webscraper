#include <iostream>
#include <string>

using namespace std;

unsigned long long arrtoint(int digits[], int numdig) {
	unsigned long long total = 0;
	for (int i = numdig - 1; i >= 0; --i) {
		total = total*10 + digits[i];
	}
	return total;
}


void backprop(int digits[], int& numdig, int pos) {
	if (pos + 1 >= numdig) {
		if (digits[pos] == 1) {
			--numdig;
			return;
		}
		else {
			digits[pos] -= 1;
			return;
		}
	}
	else {
		if (digits[pos + 1] == digits[pos]) {
			digits[pos] = 9;
			backprop(digits, numdig, pos + 1);
			return;
		}
		else {
			digits[pos] -= 1;
			return;
		}
	}
}

unsigned long long firstpass(int digits[], int numdig) {
	int prev, curr;
	prev = digits[numdig - 1];
	for (int i = numdig - 2; i >= 0; --i) {
		if (digits[i] < prev) {
			for (int j = i; j >= 0; --j) {
				digits[j] = 9;
			}
			backprop(digits, numdig, i + 1);
			break;
		}
		
		prev = digits[i];
	}
	return arrtoint(digits, numdig);
}


int main() {
	int t, numdig;
	unsigned long long n;
	int digits[20];
	
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		numdig = 0;
		
		for (int count = 0; n != 0; ++count) {
			digits[count] = n % 10;
			++numdig;
			n /= 10;
		}
		

		cout << "Case #" << i << ": " << firstpass(digits, numdig) << endl;
	}
	return 0;
}