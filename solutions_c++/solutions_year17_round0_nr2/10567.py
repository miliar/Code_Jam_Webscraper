#include <iostream>
using namespace std;

bool isTidy(int number) {
	int dividedNumber = number;
	int lastDigit = number % 10;
	//cout << "isTidy: " << number << endl;

	while(dividedNumber > 0) {
		//cout << "dividedNumber: " << dividedNumber << endl;
		int res = dividedNumber % 10;
		if (lastDigit < res)
			return false;
		else
			lastDigit = res;
		dividedNumber = (int) (dividedNumber / 10);
	}
	return true;
}

int lastTidyNumber(int number) {
	//cout << "lastTidyNumber: " << number << endl;
	int lastTidyNumber = 1;
	for(int i = lastTidyNumber; i <= number; i++)
		if(isTidy(i))
			lastTidyNumber = i;
	
	return lastTidyNumber;
}

int main() {
	int t, n;
	cin >> t; 
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		cout << "Case #" << i << ": " << lastTidyNumber(n) << endl;
	}
	return 0;

}
