#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void print_last_tidy(unsigned long long int num);
void break_num(unsigned long long int num, vector<int> & digits);
void correct_digits(vector<int> & digits);

int main() {
	
	int T;
	unsigned long long int num;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> num;
		cout << "Case #" << i << ": ";
		print_last_tidy(num);	
		cout << endl;
	}
	
	return 1;
}

/*
 * Calculate the last tidy number by scanning two digits 
 * at a time and checking for tidyness
 * Has to do go back for tidyness after correction
 * 
 */
void print_last_tidy(unsigned long long int num) {
	
	vector<int> digits;
	break_num(num, digits);
	correct_digits(digits);
}

/*
 * Correcting digits recursively
 */
void correct_digits(vector<int> & digits) {
	
	int len = digits.size();
	for (int i = 0; i < len-1; i++) {
		if (digits[i] < digits[i+1]) {
			// decrease digits
			digits[i+1]--;
			for (int j = i; j >= 0; j--)
				digits[j] = 9;
		}
	}
	// printing vector
	int j = len-1;
	while (digits[j] == 0)
		j--;
	for (int i = j; i >= 0; i--)
		cout << digits[i];
}

/*
 * Break apart number into vector of ints
 */
void break_num(unsigned long long int num, vector<int> & digits) {
	
	for (int i = 0; num > 0; i++) {
		digits.push_back(num % 10);
		num /= 10;
	}
}