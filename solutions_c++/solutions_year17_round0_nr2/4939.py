#include <iostream>
#include <string>
using namespace std;



int main() {

	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i) {
		string input;
		string output = "";

		cin >> input;


		int mostSignificantSafeDigit = 0;
		int bestDigit = input.at(0)-48;
		bool isProblem = false;
		for(int p = 1; p < input.size(); ++p) {
			int testDig = input.at(p) - 48;
			if(testDig < bestDigit) {
				isProblem = true;
				break;
			}
			if(testDig > bestDigit) {
				//cout << "better" << endl;
				bestDigit = testDig;
				mostSignificantSafeDigit = p;
				// cout << bestDigit << endl;
				// cout << mostSignificantSafeDigit << endl;
			}
		}




		cout << "Case #" << i+1 << ": ";
		if(!isProblem) {
			cout << input;
		} else {
			for(int p = 0; p < input.size(); ++p) {
				if(p < mostSignificantSafeDigit) {
					cout << input.at(p);
				} else if(p == mostSignificantSafeDigit) {
					if(p == 0 && input.at(p)-48 == 1) {
						continue;
					} else {
						int d = input.at(p) - 48;
						if(p == input.size()-1) {
							cout << d;
						} else {
							cout << d-1;
						}
					}
				} else {
					cout << "9";
				}
			}
		}

		cout << endl;
	}
	

}




