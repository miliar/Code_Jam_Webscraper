#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <limits.h>
#include <assert.h>
#include <stack>
#include <cmath>
#include <iomanip>
using namespace std;

int get_first_decreasing_index(string& s) {
	int index = 0;
	int last_index = 0;
	int i = 1;
	for(; i < s.length(); ++i) {
		if(s[i - 1] > s[i]) {
			index = last_index;
			break;
		} else if(s[i - 1] < s[i]) {
			last_index = i;
		}
	}
	if(i == s.length()) {
		index = -1;
	}
	return index;
}

int main () {
	long long t;
	cin >> t;
	for(long long tcase = 0; tcase < t; ++tcase) {
		string s;
		cin >> s;
		string result = s;
		int index = get_first_decreasing_index(s);
		if(s.length() > 1 && index >= 0) {
			if(s[index] == '1') {
				result = string(s.length() - 1, '9');
			} else {
				result[index] = result[index] - 1;
				result = result.substr(0, index + 1) + string(result.length() - index - 1, '9');
			}
		}
		cout << "Case #" << tcase + 1 << ": " << result << "\n";
	}
}
