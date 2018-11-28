#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <memory.h>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		string s;
		cin >> s;
		bool ok = true;
		for (int i = 1; i < s.length(); i++) {
			if (s[i] < s[i - 1]) {
				ok = false;
				break;
			}
		}
		
		for (int i = 1; i < s.length(); i++) {
			if (s[i] < s[i - 1]) {
				int pos = i - 1;
				while (pos > 0 && s[pos] == s[pos - 1]) {
					pos--;
				}
				s[pos]--;
				for (int j = pos + 1; j < s.length(); j++) {
					s[j] = '9';
				}
				if (s[0] == '0') {
					s = s.substr(1);
				}
				break;
			}
		}

		cout << "Case #" << test + 1 << ": " << s << endl;
	}


	//system("pause");
	return 0;
}