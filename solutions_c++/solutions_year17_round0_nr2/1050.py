//============================================================================
// Name        : B_tidy.cpp
// Author      : Oliver Roese
//============================================================================
#include <iostream>
#include <cassert>

#include <algorithm>

using namespace std;

string makeTidy(const string& nr) {
	string res;
	const int len = nr.length();

	assert(len > 0);
	assert(nr[0] != '0');
	assert(all_of(nr.begin(),nr.end(), [](char c) {return '0'<=c && c <='9';}));

	int lastTidy = 0;
	while(lastTidy+1<len && nr[lastTidy]<=nr[lastTidy+1]) {
		++lastTidy;
	}

	if (lastTidy == len-1) {
		res = nr;
	} else {
		while (lastTidy > 0 && nr[lastTidy] == nr[lastTidy-1]) {
			--lastTidy;
		}
		if (nr[lastTidy] == '1') {
			res.resize(len-1);
			fill(res.begin(), res.end(), '9');

		} else {
			res.resize(len);

			copy(nr.begin(), nr.begin()+lastTidy, res.begin());
			res[lastTidy] = nr[lastTidy] - 1;
			fill(res.begin()+lastTidy+1, res.end(), '9');
		}
	}

	return res;
}

void processTidyNumbers() {
	unsigned T = 0;
	cin >> T;
	assert(1<=T && T<=100);
	for (unsigned i = 0; i < T; ++i) {
		string nr;
		cin >> nr;
		printf("Case #%d: ", i+1);
		cout << makeTidy(nr) << "\n";
	}
}

int main() {
	processTidyNumbers();

	return 0;
}
