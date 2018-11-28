#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <deque>
#include <cassert>
#include <bitset>
#include <regex>
//#include <unordered_set>
//#include <array>
//#include <unordered_map>

using namespace std;

#define BIG_PRIME 1000000007

typedef unsigned long long ull;

bool cmpDouble(const double& a, const double& b) {
	return std::fabs(a - b) < std::numeric_limits<double>::epsilon();
}

int main() {
	
	int numOfTestCases;
	cin >> numOfTestCases;
	for (int loopTestCases = 0; loopTestCases < numOfTestCases; ++loopTestCases) {
		cout << "Case #" << loopTestCases + 1 << ": ";
		
		char tmp[1001];
		scanf("%s", tmp);
		string s = tmp;

		int k; scanf("%d", &k);
		int ct = 0;
		for (int i = 0; i <= s.size() - k; ++i) {
			if (s[i] == '-') {
				ct++;
				for (int j = 0; j < k; ++j) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
			}
		}
		
		bool fl = false;
		for (int i = s.size() - k; i < s.size(); ++i) {
			if (s[i] == '-') {
				printf("IMPOSSIBLE\n");
				fl = true;
				break;
			}
		}

		if (!fl) printf("%d\n", ct);

	
	}

}

