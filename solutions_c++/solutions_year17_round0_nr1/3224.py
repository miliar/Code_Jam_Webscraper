/*
 * main.cu
 *
 *  Created on: Apr 7, 2017
 *      Author: hexafraction
 */
#include <iostream>
#include <climits>
using namespace std;

int recurse(int, int, int, int, int);

int main() {

	int numSets;
	cin >> numSets;
	//cout << numSets << endl;
	for (int i = 0; i < numSets; i++) {
		string str;
		int k;
		cin >> str;
		cin >> k;
		// cout << str <<endl << k << endl;
		int mask = (1 << k) - 1;
		int num = 0;
		for (int q = 0; q < str.length(); q++) {

			num <<= 1;
			if (str[q] != '+') {
				num += 1;
			}
		}
		//cerr << ":" << num <<endl;
		int rslt = recurse(num, mask, 0, str.length() - k + 1, 0);
		if (rslt != INT_MAX) {
			cout << "Case #" << (i + 1) << ": " << rslt << endl;
		} else
			cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
	}
}

int recurse(int num, int mask, int count, int itersLeft, int itersDone) {
	if (num & ((1 << itersDone) - 1)) {
		return INT_MAX;
	}
	if (itersLeft == 0) {
		//cerr << num << endl;
		if (num == 0)
			return count;
		else
			return INT_MAX;
	} else {
		return min(
				recurse(num ^ mask, mask << 1, count + 1, itersLeft - 1,
						itersDone + 1),
				recurse(num, mask << 1, count, itersLeft - 1, itersDone + 1));
	}
}
