#include <iostream>
// #include <string>
// #include <map>
#include <vector>
// #include <list>
// #include <pair>
#include <tgmath.h>

using namespace std;

long solve_B(long n);
long solve_B_big(long n);

int main() {
	int len;
	vector<long> in;
	
	cin >> len;
	for (int i = 1; i <= len; ++i) {
		long n;
		
		cin >> n;
		in.push_back(n);
	}
	
	for (int i = 0; i < len; ++i) {
		long sol = solve_B_big(in[i]);
		cout << "Case #" << i + 1 << ": " << sol;
		if(i != len - 1)
			cout << endl;
	}
	
	return 0;
}

long solve_B(long n) {
	for (long i = n; i > 0; i--) {
		long num = i;
		long prev = 9;
		bool is_tidy = true;
		while(num > 0) {
			int digit = num % 10;
			if(digit > prev) {
				is_tidy = false;
				break;
			}
			num = num / 10;
			prev = digit;
		}
		if (is_tidy)
			return i;
	}
}

long solve_B_big(long n) {
	while (n > 0) {
		long num = n;
		int prev = 10;
		bool is_tidy = true;
		int exp = -1;
		int sim = 0;
		while(num > 0) {
			int digit = num % 10;
			if(digit > prev) {
				is_tidy = false;
				break;
			}
			if (digit == prev) { 
				sim++;
			} else {
				sim = 0;
			}
			num = num / 10;
			exp += 1;
			prev = digit;
		}
		if (is_tidy)
			return n;
		
		long accum = n % long(pow(10, exp - sim));
		n = n - long( ((prev) * pow(10, exp - sim)) ) - accum - 1;
	}
}
