#include <iostream>

using namespace std;

bool isTidy(long n) {
	long a = 10;
	long b = n%10;
	bool tidy = true;
	while(a <= n*10) {
		long c = n%a/(a/10);
		//cout << "b: " << b << endl;
		//cout << "c: " << c << endl;
		if(c > b) {
			tidy = false;
			//cout << "FAILED!" << endl;
			break;
		}
		b = min(b,c);
		a *= 10;
	}
	//cout << "isTidy a is " << a << endl;
	//cout << "isTidy n is " << n << endl;
	return tidy;
}

int main() {
	int t;
	cin >> t;
	for(int caseNum = 0; caseNum < t; caseNum++) {
		//cout << caseNum << endl;
		long n;
		cin >> n;
		//cout << n << " " << isTidy(n) << endl;
		while(!isTidy(n)) {
			int a = 10;
			while(n%a/(a/10) == 9) {
				a *= 10;
			}
			//cout << "take away " << (n%a/(a/10) + 1) << endl;
			//cout << "from " << n << endl;
			n = n - (n%a/(a/10) + 1);
			//cout << "to give " << n << endl;
			//cout << "a is " << a << endl;
			//cout << "isTidy(n) gives " << isTidy(n) << endl;
		}
		cout << "Case #" << caseNum+1 << ": " << n << endl;
	}
}
