#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

bool is_tidy(int N) {
	int num_digits = floor(log10(N)) + 1;
	
	bool tidy = true;
	
	int* digits = new int[num_digits];
	for (int i = 0; i < num_digits; i++) {
		int place = pow(10, num_digits-i-1);
		digits[i] = N / place;
		N -= digits[i]*place;
	}
	
	for (int i = 0; i < num_digits-1; i++) {
		if (digits[i] > digits[i+1]) {
			tidy = false;
		}
	}
	
	delete digits;
	
	return tidy;
}

int main()
{
	int T;
	int N;
	cin >> T;
	
	for (int i = 1; i <= T; ++i) {
		cin >> N;
		
		while (true) {
			if (is_tidy(N)) {
				break;
			}
			N--;
		}
		
		cout << "Case #" << i << ": " << N << endl;
	}
	
	return 0;
}