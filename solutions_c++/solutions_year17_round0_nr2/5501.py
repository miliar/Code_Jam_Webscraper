#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;

bool isTidyNumber(long long n) {
	int last = 9;
	while (n > 0) {
		if (last < n % 10) {
			return false;
		}
		last = n % 10;
		n /= 10;
	}
	return true;
}

long long solve(long long n) {
	if (isTidyNumber(n)) {
		return n;
	}
	long long p = 1;
	long long suffix = 0;

	while (n / p > 0) {
		long long prefix = n / p - 1;
		long long number = prefix * p + suffix;
		if (isTidyNumber(number)) {
			return number;
		}
		p *= 10;
		suffix = suffix * 10 + 9;
	}
}

long long brute(long long n) {
	for(long long i = n; i>=0; i--)
		if (isTidyNumber(i)) {
			return i;
		}
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long n;
		cin >> n;
		cout << "Case #" << t << ": " << solve(n) << endl;
		//if (solve(n) != brute(n)) cout << "WA" << endl;
		//cout << solve(n) << " " << brute(n) << endl;
	}
	return 0;
}
