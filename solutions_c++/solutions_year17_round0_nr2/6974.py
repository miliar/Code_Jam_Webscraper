#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

int t, k;
string str;

void pending() {

}

void fun () {
	for (int i = str.length() - 1; i > 0; i -- ) {
		if (str[i] < str[i - 1]) {
			// str[i] = '9';
			for (int j = i; j < str.length(); j ++ ) 
				str[j] = '9';
			if (str[i - 1] == '0') {
				str[i - 1] = '9';
			} else {
				str[i - 1] = str[i - 1] - 1;
			}
		}
	}
	int st = 1;
	for (int i = 0; i < str.length(); i ++ ) {
		if (str[i] == '0' && st == 1) {
			st = 1;
		} else {
			st = 0;
			cout << str[i];
		}		
	}
	cout << endl;
	// cout << str << endl;
}

int main () {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t ; i ++ ) {
		cin >> str;
		cout << "Case #" << i + 1 << ": ";
		fun();
	}
	return 0;
}

