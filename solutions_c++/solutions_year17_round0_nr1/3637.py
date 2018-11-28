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
		int k;
		cin >> s >> k;
		bool ok = true;
		int ans = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				if (i + k - 1 < s.length()) {
					for (int j = 0; j < k; j++) {
						s[i + j] = (s[i + j] == '+' ? '-' : '+');
					}
					ans++;
				}
				else {
					ok = false;
					break;
				}
			}
		}

		cout << "Case #" << test + 1 << ": ";
		if (ok) {
			cout << ans;
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}


	//system("pause");
	return 0;
}