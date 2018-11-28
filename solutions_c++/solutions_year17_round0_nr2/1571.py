//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;
#define MAXN 2010
#define oo 1e9
#define MOD 1000000007
typedef long long LL;
bool check(LL n) {
	int last = 9;
	while (n > 0) {
		int tmp = n % 10;
		if (tmp > last) {
			return false;
		}
		last = tmp;
		n /= 10;
	}
	return true;
}
int get_digit(LL n, int pos) {
	vector<int> arr;
	while (n > 0) {
		arr.push_back(n % 10);
		n /= 10;
	}
	return arr[pos];
}
LL set_digit(LL n, int pos, int digit) {
	vector<int> arr;
	while (n > 0) {
		arr.push_back(n % 10);
		n /= 10;
	}
	arr[pos] = digit;

	LL ans = 0;
	for (int i = arr.size() - 1; i >= 0; --i) {
		ans = ans * 10 + arr[i];
	}
	return ans;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		LL n;
		cin >> n;
		LL ans = n;
		for (int i = 0; ans > n || !check(ans); ++i) {
			if (ans > n) {
				int digit = get_digit(ans, i);
				ans = set_digit(ans, i, (digit - 1 + 10) % 10);
			}
			if (!check(ans)) {
				ans = set_digit(ans, i, 9);
			}
		}
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}
