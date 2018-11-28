#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <limits.h>

using namespace std;

int result = INT_MAX;
bool isAllHappy(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			return false;
		}
	}
	return true;
}

void calculate(string s, int k, int steps, int index) {


	if (isAllHappy(s)) {
		result = min(steps, result);
		return;
	}

	for (int i = index + 1; i <= (int)s.size() - k; i++) {
		string tmp = s;
		for (int j = i; j < i + k; j++) {
			if (tmp[j] == '+') {
				tmp[j] = '-';
			} else {
				tmp[j] = '+';
			}
		}
		calculate(tmp, k, steps + 1, i );
	}

}

int main() {
	freopen("test.in", "rt", stdin);
	freopen("test.out", "w", stdout);

	int t = 0, case_num = 1;

	string s;
	int k = 0;
	cin >> t;

	while (case_num <= t) {

		cin >> s >> k;
		result = INT_MAX;
		calculate(s, k, 0, -1);

		cout << "Case #" << case_num << ": " ;
		if(result == INT_MAX){
			cout << "IMPOSSIBLE";
		}else {
			cout << result;
		}
		cout << endl;
		case_num++;
	}

	return 0;
}
//By : mohamed waleed
