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

long long lastNumber;

long long solve() {
	string strLastNumber = to_string(lastNumber);

	while (true) {
		bool sorted = true;
		for (int i = 0; i < strLastNumber.length()-1; i++) {
			if (strLastNumber[i] > strLastNumber[i + 1]) {
				sorted = false;
				strLastNumber[i] = strLastNumber[i] - 1;
				for (int j = i + 1; j < strLastNumber.length(); j++) {
					strLastNumber[j] = '9';
				}
				break;
			}
		}
		if (sorted) {
			return stoll(strLastNumber);			
		}
	}
}

void main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int testCase;
	cin >> testCase;
	for (int t = 1; t <= testCase; t++) {
		cin >> lastNumber;
		printf("Case #%d: ", t);
		cout << solve() << endl;
	}
}