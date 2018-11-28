#include <iostream>
#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstring>
#include <map>
#include <numeric>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

string cakes;
int flipperSize;

void flip(int index, int size) {
	int flipCount = 0;
	while (flipCount < size) {
		if (cakes[index] == '-')
			cakes[index] = '+';
		else
			cakes[index] = '-';

		index++;
		flipCount++;
	}
}

int solve() {
	int answer = 0;
	for (int i = 0; i < cakes.length(); i++) {
		if (cakes[i] == '-') {
			if (cakes.length() - i < flipperSize)
				return -1;

			flip(i, flipperSize);
			answer++;
		}
	}

	return answer;
}

void main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int testCase;
	cin >> testCase;
	for (int t = 1; t <= testCase; t++) {
		cin >> cakes >> flipperSize;
		printf("Case #%d: ", t);
		int answer = solve();
		if (answer == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << answer << endl;
	}
}