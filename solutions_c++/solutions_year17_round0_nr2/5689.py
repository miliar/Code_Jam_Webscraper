#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;
typedef long long LL;
typedef vector<LL> VL;
typedef vector<VL> VVL;
LL TidyNumber(LL number) {
	VVL v;
	LL part = number;
	LL multiplier = 1;
	while (part != 0) {
		LL digit = part % 10;
		part /= 10;
		VL vt({digit, multiplier});
		v.push_back(vt);
		multiplier *= 10;
	}
	while (true) {
		int i = 0;
		while (i + 1 < v.size() && v[i][0] >= v[i + 1][0]) ++i;
		if (i + 1 >= v.size()) break;
		--v[i + 1][0];
		int right = v.size() - 1;
		for (int j = 0; j <= i; ++j) v[j][0] = 9;
		while (right >= 0 && v[right--][0] == 0) v.pop_back();
	}
	LL result = 0;
	for (int i = 0; i < v.size(); ++i) {
		result += v[i][0] * v[i][1];
	}
	return result;
}
void TestTidyNumbers() {
	int T;
	LL N;
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
	cin >> T;
	for (int qq = 1; qq <= T; ++qq) {
		cin >> N;
		LL result = TidyNumber(N);
		cout << "Case #" << qq << ": " << result << "\n";
	}
	fflush(stdout);
}