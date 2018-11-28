/*
 * 1.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: atulb
 */

#include <bits/stdc++.h>

using namespace std;

using LL = long long;
using ULL = unsigned long long;
#define vi vector<LL>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"

void solve(LL casenum) {
	cout << "Case #" << casenum << ": ";

	string s;
	cin >> s;

	LL sz = s.size();

	LL i = 0;

	while (i <= sz - 2 && s[i] <= s[i + 1])
		++i;

	if (i == sz - 1) {
		cout << s << endl;
		return;
	}

	assert(s[i+1] < s[i]);

	LL j = i;
	while (j - 1 >= 0 && s[j - 1] == s[i])
		j--;

	assert(s[j] == s[i]);

	s[j] = char(int(s[j]) - 1);
	for (LL x = j + 1; x < sz; ++x)
		s[x] = '9';

	if (j == 0 && s[j] == '0')
		s = s.substr(1);

	assert(s[0] != '0');

	cout << s << endl;
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	LL T;
	cin >> T;
	for (LL i = 1; i <= T; ++i) {
		solve(i);
	}

	return 0;
}
