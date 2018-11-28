#include <iostream>
#include <string>
#include <sstream>

bool is_tidy(std::string &s) {
	for (unsigned int i = 1; i < s.length(); i++)
		if (s[i-1] > s[i]) return false;
	return true;
}

unsigned int long long construct_largest_tidy_number(unsigned long long int n) {
	if (n == 0) return 0;
	if (n < 10) return n;
	
	std::string s = std::to_string(n), a;
	char previous_digit, digit;
	unsigned int i;

	if (is_tidy(s)) return n;

	//std::cout << "n = " << n << std::endl;
	//std::cout << "s = " << s << std::endl;

	previous_digit = s[0];
	for (i = 1; i < s.length(); i++) {
		digit = s[i];
		//std::cout << "previous = " << previous_digit << std::endl;
		//std::cout << "current = " << digit << std::endl;
		if (digit >= previous_digit) {
			a.push_back(previous_digit);
		} else {
			if ('0' == previous_digit) {
				a.push_back('0');
				for (; i < s.length(); i++) a.push_back('9');
				break;
			} else {
				previous_digit--;
				a.push_back(previous_digit);
				if (2 <= a.length()) {
					while (a[a.length()-1] < a[a.length()-2]) {
						a.pop_back();
						a[a.length()-1]--;
						i--;
						if (1 == a.length()) break;
					}
				}
				for (; i < s.length(); i++) a.push_back('9');
				break;
			}
		}
		previous_digit = digit;
	}

	//std::cout << "a = " << a << std::endl;	

	unsigned long long int e = 0;
	unsigned long long int power = 1;
	//*
	for (int j = a.length() - 1; j >= 0; j--) {
		e += power*(a[j]-48);
		power *= 10;
	}
	//*/

	return e;
}

int main() {
	unsigned int T;
	unsigned long long int N;

	std::cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		std::cin >> N;

		std::cout << "Case #" << i + 1 << ": " << construct_largest_tidy_number(N) << std::endl;
	}

	return 0;
}
