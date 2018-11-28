#include <iostream> 
#include <stdlib.h>
#include <string>
#include <math.h>

using namespace std;
unsigned long long findClosestTidy(unsigned long long num);

void main() {

	unsigned long long int n, num;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		printf("Case #%d: %I64d\n", i + 1, findClosestTidy(num));
	}

}

unsigned long long findClosestTidy(unsigned long long num) {
	
	unsigned long long divider = pow(10, (int)log10(num));
	int digit;
	for (int i = 0; i < (int)log10(num); i++) {
		digit = num / divider % 10;
		int secondDigit = (num / (divider / 10) % 10);
		if (digit > secondDigit) {
			num = ((num / divider) * divider) - 1;
			num = findClosestTidy(num);
		}
		divider = divider / 10;
	}
	return num;

}

