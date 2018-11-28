#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
#include <iomanip>      // std::setprecision
using namespace std;  // since cin and cout are both in namespace std, this saves some text

void main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		double d;
		int n;
		double k[1001], s[1001];
		cin >> d >> n;
		for (int i = 0; i < n; i++) {
			cin >> k[i] >> s[i];
		}
		double maxTime = 0;
		for (int i = 0; i < n; i++) {
			//cout << d - k[i] << endl;
			//cout << (d - k[i]) / s[i] << endl;
			double tmax = (d - k[i]) / s[i];
			if (tmax > maxTime)
				maxTime = tmax;
		}
		//cout << maxTime << endl;

		std::cout << std::fixed;
		std::cout << std::setprecision(6);
		cout << "Case #" << i << ": " << (d / maxTime) << endl;
	}
}