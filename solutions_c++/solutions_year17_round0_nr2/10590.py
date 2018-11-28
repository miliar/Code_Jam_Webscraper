#include <iostream>

using namespace std; 

void main() {
	int t, curDig, nextDig;
	long long int n;
	cin >> t; 
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		for (int i = 1; i < log10(n) + 1; i++)
		{
			curDig = n % ((int)pow(10,i));
			if (i >= 2) curDig /= (int)pow(10,(i - 1));
			nextDig = ((n % ((int)pow(10,(i+1)))) / (int)pow(10,i));
			if (curDig < nextDig)
				n -= (n % (int)pow(10,i) + 1);
		}
		cout << "Case #" << i << ": " << n << endl;
	}
}