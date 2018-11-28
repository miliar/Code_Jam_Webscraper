#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <tuple>
#include <algorithm>
#include <iterator>
#include <string>
#include <iostream>
#include <fstream>
#include <cassert>

using namespace std;

typedef long long int lli;

bool checkPow(lli k, lli i) {
	return 1ll << i == k;
}

lli getPow(lli k) {
	lli pow = 0;
	while (k >>= 1) {
		pow++;
	}

	return pow;
}

pair<lli, lli> solve(lli n, lli k) {
	lli i = 0;
	lli mx = n, mn = n;

	lli kcpy = k;

	while (i < getPow(k)) {
		mn = (mx - 1) / 2;
		mx = (mx - 1) / 2 + (mx - 1) % 2;
		
		if (kcpy % 2) {
			mx = mn;
		}

		kcpy >>= 1;

		i++;
	}

	mn = (mx - 1) / 2;
	mx = (mx - 1) / 2 + (mx - 1) % 2;
	
	return { max(mx, 0ll), max(mn, 0ll) };
}

int main() {
	ifstream fin("in.in");
	ofstream fout("out.out");

	//for (int i = 0; i < 20; i++) {
	//	cout << i << ": " << getPow(i) << endl;
	//}

	int test_number;
	fin >> test_number;
	for (int test_i = 0; test_i < test_number; test_i++) {
	/*while (1) {*/
		lli n, k;
		fin >> n >> k;

		auto answer = solve(n, k);

		fout << "Case #" << test_i + 1 << ": " << answer.first << " " << answer.second << endl;
	}
	
	system("pause");
	return 0;
}