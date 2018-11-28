#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
using namespace std;

int t, k, length;

string swap(string str, int index) {
	for (int i = index; i < index + k; i++) {
		str[i] = (str[i] == '+' ? '-' : '+');
	}
	return str;
}

int main()
{
	cin >> t;
	for (int testcase = 0; testcase < t; testcase++) {
		string state;
		cin >> state >> k;
		length = state.length();
		string result(length, '+');
		if (state == result) {
			cout << "Case #" << testcase + 1 << ": " << 0 << endl;
			continue;
		}
		int step = 0;
		for (int i = 0; i < length - k + 1; i++) {
			if (state[i] == '+') {
				continue;
			}
			else {
				state = swap(state, i);
				step++;
			}
			//cout << state << endl;
		}

		if (state == result) {
			cout << "Case #" << testcase + 1 << ": " << step << endl;
		}
		else {
			cout << "Case #" << testcase + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}