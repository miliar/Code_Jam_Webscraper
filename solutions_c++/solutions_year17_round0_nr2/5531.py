#include <iostream>
using namespace std;


long long isTidy(long long n) {
	int lastDigit = 10;
	long long sub = 1;
	while(n) {
		int currentDigit = n % 10;
		if (currentDigit > lastDigit)
			return 1;
		lastDigit = currentDigit;
		n /= 10;
		sub *= 10;
	}
	return 0;
}

int main() {
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		long long n;
		cin >> n;
		long long result = n;
		while(true){
			long long s = isTidy(result);
			result -= s;
			if (!s)
				break;
		}
		cout << "Case #" << test+1 << ": " << result << endl;
	}
}