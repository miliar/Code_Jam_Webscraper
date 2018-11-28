#include <iostream>

using namespace std;

bool isTidy(long long n) {
	int cifbefore = 9;
	long long nO = n;
	while (n > 0) {
		if (n%10 > cifbefore) {
			//cout << nO << " is NOT tidy" << endl;
			return false;
		}
		cifbefore = n%10;
		n/=10;
	}
	//cout << nO << " is tidy" << endl;
	return true;
}

long long last(long long n) {
	if (isTidy(n)) {
		return n;
	}
	return last(n-(n%10+1));
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i<t; i++) {
		long long n;
		cin >> n;
		cout << "Case #" << i+1 << ": " << last(n) << endl;
	}
}