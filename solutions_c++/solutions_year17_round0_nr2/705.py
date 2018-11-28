#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void solve() {
	string input;
	cin >> input;
	int size = input.length();
	if (size == 1) {
		cout << input << endl;
		return;
	}
	for (int c = size-1; c > 0; c--) {
		if (input[c] < input[c - 1]) {
			for (int d = c; d < size; d++) {
				input[d] = '9';
			}
			input[c-1] = input[c-1] - 1;
		}
	}
	int leadingZeroes = 0;
	while (input[leadingZeroes] == '0') leadingZeroes++;
	input.erase(0,leadingZeroes);
	cout << input << endl;
}


int main() {
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; i++) {
    	cout << "case #" << i << ": ";
    	solve();
	} 
}
