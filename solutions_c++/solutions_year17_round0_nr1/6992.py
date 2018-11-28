#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

int t, k;
string str;

void fun () {
	int counter = 0;
	int st = 1;
	for (int i = 0; i < str.length(); i ++ ) {

		if (str[i] == '-') {
			if (i + k > str.length()) {
				st = 0;
				break;
			}
			counter ++;
			for (int j = 0; j < k; j ++ ) {
				if (str[i + j] == '+') {
					str[i + j] = '-';
				} else {
					str[i + j] = '+';
				} 
			}
		}
	}
	if (st) {
		cout << counter << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main () {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t ; i ++ ) {
		cin >> str >> k;
		cout << "Case #" << i + 1 << ": ";
		fun();
	}
	return 0;
}

