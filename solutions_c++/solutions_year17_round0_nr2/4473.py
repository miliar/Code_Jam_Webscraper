#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		string n;
		cin >> n;
		ostringstream y;
		bool isLower = false;
		int repeatDigit = 9;
		for(int i = 0; i < n.length(); i++) {
			if(!isLower) {
				int digit = n[i] - '0';
				if(i == n.length() - 1) {
					y << digit;
				}
				else {
					int nextDigit = n[i+1] - '0';
					if(digit < nextDigit)
						y << digit;
					else if(digit > nextDigit) {
						if(digit > 1)
							y << digit - 1;
						isLower = true;
					}
					else {
						bool stoppedRepeating = false;
						for(int j = i + 2; j < n.length(); j++) {
							nextDigit = n[j] - '0';
							if(digit < nextDigit) {
								y << digit;
								stoppedRepeating = true;
								break;
							}
							else if(digit > nextDigit) {
								if(digit > 1)
									y << digit - 1;
								isLower = true;
								stoppedRepeating = true;
								break;
							}
						}
						if(!stoppedRepeating) {
							y << digit;
							repeatDigit = digit;
							isLower = true;
						}
					}
				}
			}
			else {
				y << repeatDigit;
			}
		}
		cout << "Case #" << caseNum << ": " << y.str() << endl;
	}
	return 0;
}
