#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <limits> 
#include <queue>

using namespace std;

string f(string s);

int main() {
	int n; // number of test cases
	scanf("%d\n", &n);

	for (int i = 0; i < n; i++) {
		string s;
		getline(cin, s);

		string res = f(s);
		if (res[0] == '0') {
			cout << "Case #" << i + 1 << ": " << res.substr(1) << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": " << res << endl;
		}
	}
	return 0;
}

string f(string s) {
	int loc = -1;
	for (int l = 1; l < s.length(); l++) {
		if ((int) s[l] < (int) s[l - 1]) {
			loc = l;
			break;
		}
	}
	if (loc == -1) return s;

	for (int l = loc; l < s.length(); l++) {
		s[l] = '9';
	}
	s[loc - 1] = s[loc - 1] - 1;
	return f(s);
}
