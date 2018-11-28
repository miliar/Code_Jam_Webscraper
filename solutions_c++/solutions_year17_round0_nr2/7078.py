// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iomanip>      // std::setprecision
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {

		char number[30];
		cin >> number;

		// Initialize the different variables to store the tidy number check state
		int startIndex = 0;
		int len = strlen(number);

		// Check all digits of the given number and see if it's tidy number
		bool tidy = true;
		for (int i=1; i< len; i++) {
			
			// If next number is larger, we are good
			if (number[i] > number [i-1]) {
				startIndex = i;
				continue;
			}
			// We reached a point, where the number should be fixed to be tidy number
			else if (number[i] < number [i-1]) {
				tidy = false;
				break;
			}
		}

		char output[30];

		// Input number is already tidy number
		if (tidy) {
			strcpy (output,number);
		} else {
			int nineCount = len - startIndex - 1;

			// If the digit position where we are splitting the number to make it tidy has 1 or 0
			// then we need to remove digit as well. For example if number is 1000. Then 
			// startIndex will be pointing to 1, so need to remove this to make number 999
			if (number[startIndex] == '1')
				startIndex--;
			else if (number[startIndex] == '0') {
				startIndex--;
				number[startIndex] = number[startIndex] - 1;
			}
			else 
				number[startIndex] = number[startIndex] - 1;

			// Now build the number with prefix and correct set of nines
			int index = 0;
			for (int i=0; i<= startIndex; i++) {
				output[index++] = number[i];
			}
			for (int i=0; i< nineCount; i++) {
				output[index++] = '9';
			}
			output[index] = 0;
		}
			
		std::cout << "Case #" << test << ": " << output << endl;
	}
}
