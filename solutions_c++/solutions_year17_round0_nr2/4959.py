#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
	int T; // number of tests
	scanf("%d", &T);
	string temp;
	getline(cin, temp);

	for (int i = 0; i < T; i++) {
		string str;
		getline(cin, str);

		int len = str.length();
		int idx = len - 1;

		if (idx == 0) {
			cout << "Case #" << i+1 << ": " << str << endl;
			continue;
		}

		idx--;
		while (idx >= 0) {
			if (str[idx] <= str[idx+1]) {
				idx--;
				continue;
			}
			for (int j = idx+1; j < len; j++) {
				str[j] = '9';
			}
			str[idx]--;
			idx--;
		}

		if (str[0] == '0') {
			cout << "Case #" << i+1 << ": " << str.substr(1, len-1) << endl;
		} else {
			cout << "Case #" << i+1 << ": " << str << endl;
		}
	}
}