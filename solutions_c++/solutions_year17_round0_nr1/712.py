#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void solve () {
	string input;
	int flipper;
	int flips = 0;
	cin >> input;
	cin >> flipper;
	
	while (input.size() > 0) {
		if (input[0] == '+') input.erase(input.begin());
		else {
		    if (input.size() < flipper) break;
		    flips++;
			for (int i = 0; i < flipper; i++){
				(input[i] == '+')?input[i] = '-':input[i] = '+';
			}
		}
	}
	if (input.size() == 0) {
		cout << flips << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; i++) {
    	cout << "case #" << i << ": ";
    	solve();
	}
	return 0; 
}

