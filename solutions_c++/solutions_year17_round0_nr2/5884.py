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


bool isTidy(int i) {
	int digits = log10(i) + 1;
	int ar[20];
	memset(ar, -1, 20*sizeof(int));
	for (int j = 1; j <= digits - 1; ++j) {
		int mod = pow(10, j);
		int tmp = (i % mod);
		ar[j - 1] = tmp;
		if (j - 1 != 0) ar[j - 1] /= (10 * (j - 1));
	}
	ar[digits - 1] = i/pow(10, digits - 1);
	for (int j = 0; j < digits - 1; ++j) {
		if (ar[j + 1] > ar[j]) return false;
	}
	return true;
}

int main() {
	
	int numOfTestCases;
	cin >> numOfTestCases;
	for (int loopTestCases = 0; loopTestCases < numOfTestCases; ++loopTestCases) {
		cout << "Case #" << loopTestCases + 1 << ": ";
	
		int n; scanf("%d", &n);

		for (int i = n; i > 0; --i) {
			if (isTidy(i)) {
				printf("%d\n", i);
				break;
			}
		}
	}

}

