#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
	//freopen("stdin.inp", "r", stdin);
	//freopen("stdout.out", "w", stdout);

	int t;
	cin >> t;

	string str;
	int k;
	int i;
	int res, count = 0;
	int flag;

	while (t--) {
		++count;
		res = 0;
		i = 0;
		flag = 0;
		cin >> str >> k;

		while (i < str.length()) {
			if (str[i] == '+') {
				if (flag > 0) {
					if (i + k - 1 < str.length()) {
						for (int j = i; j < i + k; j++) {
							str[j] = '-' + '+' - str[j];
						}
						++res;
					}
					else {
						break;
					}
				}
				else {
					++i;
				}
			}
			else {
				++flag;
				if (flag == k) {
					++res;
					flag = 0;
				}
				++i;
			}
		}
		if (flag > 0) {
			cout << "Case #" << count << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << count << ": " << res << endl;
		}
	}
	return 0;
}