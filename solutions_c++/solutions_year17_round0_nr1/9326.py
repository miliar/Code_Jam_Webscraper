#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <ctype.h>
#include <list>
#include <stack>
#include <forward_list>
#include <algorithm>
#include <fstream>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <utility>

using namespace std;

static int countflips(string &s, int k) {
	vector<int> sw(1001, 0);
	int i = 0, j;
	int flips = 0;
	int start;
	int flipcount = 0;
	bool notpossible = false;
	for (i = 0; i < s.size(); i++) {
		start = (i - k + 1 < 0) ? 0 : i - k + 1;
		flips = 0;
		for (j = i - 1; j >= start; j--) {
			flips += sw[j];
		}
		if ((s[i] == '+' && flips % 2 != 0) || (s[i] == '-' && flips % 2 == 0)) {
			if (i >= (s.size() - k + 1)) {
				notpossible = true;
				break;
			}
			flipcount++;
			sw[i] = 1;
		}
	}
	if (!notpossible)
		return flipcount;
	return -1;
}

int main() {
	int i, k = 4;
	int num_test = 1;
	int flips = 0;
	string s;
	string impos = "IMPOSSIBLE";
	cin >> num_test;
	for (i = 1; i <= num_test; i++) {
		s.clear();
		cin >> s;
		cin >> k;
		flips = countflips(s, k);
		if (flips >= 0)
			cout << "Case #" << i << ": " << flips << endl;
		else
			cout << "Case #" << i << ": " <<impos<< endl;
	}
	return 0;
}
