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
	int i, j;
	int count = 0;

	while (t--) {
		++count;
		cin >> str;
		str = '0' + str;
		j = str.length();
		for (i = 0; i < str.length() - 1; i++) {
			if (str[i] > str[i + 1]) {
				j = i;
				while (str[j - 1] == str[j]) {
					j--;
				}
				str[j]--;
				str = str.substr(0, j + 1) + string(str.length() - j - 1, '9');
				break;
			}
		}
		while (str[0] == '0') {
			str = str.substr(1, str.length() - 1);
		}
		cout << "Case #" << count << ": " << str << endl;
	}

	return 0;
}