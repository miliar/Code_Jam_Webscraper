#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
using namespace std;
int main() {
	int numTests;
	cin >> numTests;
	for (int test = 0; test < numTests; test++) {
		string number;
		long long r = 0;
		cin >> number;
		int last = number.length();
		for (int i = 1; i < number.length(); i++) {
			if (number[i] < number[i - 1]) {
				last = i;
				break;
			}
		}
		if (last == number.length()) {
			cout<< "Case #" << (test + 1) <<  ": " <<  number << "\n";
		}
		else {
		//r: 0~last-1 bits
			int last2 = 0;
			for (int i = last - 1; i > 0; i--) {
				if (number[i] - '0' - 1 >= number[i - 1] - '0') {
					last2 = i;
					break;
				}
			} 	
			for (int i = 0; i <= last2; i++) {
				r = r * 10 + number[i] - '0';
			}
			for (int i = 0; i < number.length() - last2 - 1; i++)
				r = r * 10;
			r = r - 1;
			cout<< "Case #" << (test + 1) <<  ": " <<  r << "\n";
		}

	}
}
