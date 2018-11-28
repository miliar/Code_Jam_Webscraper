#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;

	for(int i = 1; i < t+1; i++) {
		string x;
		cin >> x;

		//find first non matching pair
		while(true) {
			int nonMatch = -1;
			for(int j = 0; j < x.size()-1; j++) {
				if(x[j] > x[j+1]) {
					nonMatch = j;
					break;
				}
			}

			if(nonMatch == -1) {
				break;
			}

			x[nonMatch] = x[nonMatch]-1;
			for(int j = nonMatch+1; j < x.size(); j++) {
				x[j] = '9';
			}

			while(x[0] == '0') {
				x.erase(0, 1);
			}
		}

		cout << "Case #" << i << ": " << x << '\n';
	}
}